# FLLC — Flipper Zero Arsenal

<div align="center">

```
    ███████╗██╗     ██╗      ██████╗
    ██╔════╝██║     ██║     ██╔════╝
    █████╗  ██║     ██║     ██║
    ██╔══╝  ██║     ██║     ██║
    ██║     ███████╗███████╗╚██████╗
    ╚═╝     ╚══════╝╚══════╝ ╚═════╝
         FLIPPER ZERO ARSENAL
```

**Custom BadUSB payloads, SubGHz captures, NFC tools, and IR databases.**

</div>

---

## FLLC Custom Payloads

### BadUSB (`FLLC_BadUSB/`)

| Payload | Target | Description | Time |
|---------|--------|-------------|------|
| `wifi_grab.txt` | Windows | Extract all saved WiFi passwords to USB | ~8s |
| `sysinfo_dump.txt` | Windows | Full system info, users, software, processes | ~12s |
| `browser_harvest.txt` | Windows | Chrome/Edge/Firefox history, cookies, logins | ~10s |
| `credential_dump.txt` | Windows | Windows Vault, cmdkey, SSH keys, RDP history | ~10s |
| `network_recon.txt` | Windows | Full network mapping, ARP, DNS cache, firewall | ~15s |
| `reverse_beacon.txt` | Windows | Encoded reverse shell beacon (set LHOST/LPORT) | ~6s |

### How It Works

1. Flipper Zero emulates a USB keyboard
2. Opens PowerShell (hidden window)
3. Executes encoded one-liner
4. Data saved to `\loot\` on the first USB drive detected
5. Cleans up temp files

### Deployment

1. Copy `FLLC_BadUSB/*.txt` to your Flipper's SD card under `badusb/`
2. On Flipper: BadUSB → Select payload → Run
3. Retrieve data from `\loot\` on the target's USB drive

---

## Original Repository Content

This repo is forked from [0dayCTF/Flipper](https://github.com/0dayCTF/Flipper) and includes the full community collection:

- **BadUSB/** — Community keystroke injection scripts
- **Sub-GHz/** — Radio frequency captures and analysis
- **NFC/** — NFC card data and tools
- **Infrared/** — IR remote databases (TV, AC, projectors)
- **GPIO/** — Hardware interface scripts
- **Applications/** — Custom Flipper apps

---

## Recommended Firmware

| Firmware | Link |
|----------|------|
| Unleashed | [DarkFlippers/unleashed-firmware](https://github.com/DarkFlippers/unleashed-firmware) |
| Momentum | [Next-Flip/Momentum-Firmware](https://github.com/Next-Flip/Momentum-Firmware) |
| Official | [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware) |

---

## Color Palette

```
Background:  #0D0D1A (Midnight)
Primary:     #00FFFF (Cyan)
Secondary:   #FF00FF (Fuchsia)
Accent:      #7B2FBE (Ultraviolet)
Text:        #E0E0FF (Ghost White)
Success:     #00FF88 (Neon Green)
Warning:     #FFB800 (Amber)
```

---

<div align="center">

**FLLC 2026 — Authorized penetration testing only.**

</div>
