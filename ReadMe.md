```
 ███████╗██╗     ██╗      ██████╗
 ██╔════╝██║     ██║     ██╔════╝
 █████╗  ██║     ██║     ██║
 ██╔══╝  ██║     ██║     ██║
 ██║     ███████╗███████╗╚██████╗
 ╚═╝     ╚══════╝╚══════╝ ╚═════╝
  FLIPPER ZERO ARSENAL — 2026
```

<p align="center">
<img src="https://img.shields.io/badge/FLLC-Flipper_Zero-00FFFF?style=for-the-badge&labelColor=0D0D2B"/>
<img src="https://img.shields.io/badge/BadUSB-Payloads-FF00FF?style=for-the-badge&labelColor=0D0D2B"/>
<img src="https://img.shields.io/badge/Sub--GHz-Radio-7B2FBE?style=for-the-badge&labelColor=0D0D2B"/>
<img src="https://img.shields.io/badge/NFC-Attacks-00FFFF?style=for-the-badge&labelColor=0D0D2B"/>
<img src="https://img.shields.io/badge/Anti--AI-Evasion-FF00FF?style=for-the-badge&labelColor=0D0D2B"/>
</p>

---

## Overview

Complete Flipper Zero payload library and reference guide. Includes original community resources plus FLLC custom tools with anti-AI evasion, polymorphic payloads, and comprehensive radio/NFC/IR attack documentation.

---

## FLLC Custom Modules

| Directory | Contents |
|-----------|----------|
| `FLLC_BadUSB/` | 6+ BadUSB payloads — WiFi grab, sysinfo dump, browser harvest, reverse beacon, credential dump, network recon |
| `FLLC_SubGHz/` | Complete frequency atlas, rolling code attack theory, protocol reference |
| `FLLC_NFC/` | Mifare Classic attack guide, NDEF injection payloads, EMV reference, magic card guide |
| `FLLC_Infrared/` | Universal IR code database, capture & replay guide, protocol reference |
| `FLLC_Tools/` | SD card organizer, polymorphic payload builder with anti-AI timing evasion |

---

## FLLC BadUSB Payloads

| Payload | Target | Description |
|---------|--------|-------------|
| `wifi_grab.txt` | Windows | Extract all saved WiFi SSIDs and passwords |
| `sysinfodump.txt` | Windows | Comprehensive system information collection |
| `browser_harvest.txt` | Windows | Browser history, bookmarks, and cookie extraction |
| `reverse_beacon.txt` | Windows | DNS-based reverse beacon for covert signaling |
| `credential_dump.txt` | Windows | Windows Credential Manager extraction |
| `network_recon.txt` | Windows | Network configuration and active connection mapping |

---

## Sub-GHz Reference

- **Frequency Atlas** — ISM bands, regional allocations, IoT protocols, garage/gate frequencies
- **Rolling Code Theory** — RollJam, RollBack, KeeLoq cryptanalysis, countermeasures
- **Protocol Reference** — OOK, ASK, FSK, GFSK, LoRa modulation types

---

## NFC Attack Reference

- **Mifare Classic** — Default keys, nested attack, darkside attack, hardnested, relay
- **NDEF Injection** — URL redirect, WiFi auto-connect, vCard injection, app launch
- **EMV Contactless** — What can/cannot be read, skimming limitations
- **Magic Cards** — Gen1a through Gen4 compatibility reference

---

## Infrared Reference

- **Universal Codes** — TV, AC, projector, soundbar codes by brand and protocol
- **Capture Guide** — Step-by-step IR signal capture, raw recording, file format

---

## Payload Builder (Anti-AI)

The `FLLC_Tools/payload_builder.py` generates polymorphic BadUSB payloads:

```bash
# Generate WiFi grabber with anti-AI timing jitter
python payload_builder.py wifi_grab -o wifi.txt --obfuscation 2

# Generate 5 unique variants of sysinfo dump
python payload_builder.py sysinfo --variants 5 -o sysinfo.txt

# List all templates
python payload_builder.py --list
```

**Anti-AI features:**
- Randomized inter-keystroke delays (defeats behavioral analysis)
- Polymorphic delay patterns (each variant is unique)
- String obfuscation levels (case mixing, concatenation splitting)
- Gaussian-distributed timing (mimics human typing patterns)

---

## Community Resources (Included)

| Directory | Source |
|-----------|--------|
| `BadUSB/` | Community DuckyScript payloads |
| `Sub-GHz/` | Regional frequency databases |
| `NFC/` | NFC card data and assets |
| `Infrared/` | IR remote databases |
| `Applications/` | .fap application files |
| `GPIO/` | GPIO pinout references and scripts |
| `Wifi_DevBoard/` | WiFi devboard (ESP32) integration |

---

## SD Card Setup

```bash
# Organize your Flipper SD card
python FLLC_Tools/sd_organizer.py E:\ --all

# This will:
#   1. Create all required directories
#   2. Move loose files to correct locations
#   3. Remove duplicates
#   4. Generate inventory report
```

---

## Legal

For authorized penetration testing and security research only.

**FLLC 2026** — FU PERSON by PERSON FU
