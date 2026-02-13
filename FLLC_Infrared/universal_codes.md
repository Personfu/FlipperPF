# FLLC Infrared Code Database Reference

> Universal IR remote codes for security research and physical penetration testing.
> FLLC 2026 — FU PERSON

---

## Overview

The Flipper Zero can capture, store, and replay infrared signals. This is useful for:
- Physical security assessments (controlling displays, projectors, AV systems)
- Social engineering (disrupting presentations, changing channels)
- Access control testing (IR-based door locks, barriers)

---

## Flipper IR File Format

```
Filetype: IR signals file
Version: 1
#
name: Power
type: parsed
protocol: NEC
address: 04 00 00 00
command: 08 00 00 00
```

---

## Universal TV Power Off Codes

The Flipper's built-in "Universal Remote" cycles through common power codes. These protocols cover most televisions:

| Brand | Protocol | Address | Power Command |
|-------|----------|---------|--------------|
| Samsung | NEC ext | 07 07 | 02 |
| LG | NEC | 04 | 08 |
| Sony | SIRC | 01 | 15 |
| Vizio | NEC | 04 | 08 |
| TCL/Roku | NEC | 04 | 08 |
| Hisense | NEC | 00 | 48 |
| Toshiba | NEC | 02 | 48 |
| Panasonic | Kaseikyo | 2002 | 3D |
| Philips | RC5 | 00 | 0C |
| Sharp | Sharp | 01 | 41 |
| JVC | JVC | 03 | 30 |

---

## Universal AC Codes

| Brand | Protocol | Notes |
|-------|----------|-------|
| Daikin | Daikin proprietary | Long packets, complex state |
| Mitsubishi | Mitsubishi Heavy | 88-bit protocol |
| LG | NEC extended | Standard power/mode commands |
| Samsung | Samsung extended | Similar to TV but different addresses |
| Carrier | NEC | Simple on/off |
| Fujitsu | Fujitsu proprietary | Temperature encoded in packet |

---

## Projector Codes

| Brand | Protocol | Power On | Power Off |
|-------|----------|----------|-----------|
| Epson | NEC | Various by model | Same |
| BenQ | NEC | 0x30/0x00 | 0x30/0x00 (toggle) |
| Optoma | NEC | Various | Various |
| ViewSonic | NEC | Various | Various |

---

## Soundbar / Audio

| Brand | Protocol | Notes |
|-------|----------|-------|
| Sonos | Doesn't use IR | WiFi only |
| Bose | Bose proprietary | Capturable |
| JBL | NEC | Standard NEC protocol |
| Samsung | Samsung IR | Matches TV address range |
| Sony | SIRC | Standard Sony protocol |
| Vizio | NEC | Shared with TV codes |

---

## Capture Workflow

1. **Flipper Zero -> Infrared -> Learn New Remote**
2. Point the original remote at Flipper's IR receiver
3. Press the button you want to capture
4. Flipper decodes the protocol, address, and command
5. Save to SD card under `/infrared/`
6. Replay anytime with **Send** function

### Raw Capture (Unknown Protocol)
If the protocol isn't recognized:
1. Use **Learn New Signal** instead of **Learn New Remote**
2. Flipper records the raw timing data
3. Save as raw — replay works but no protocol info

---

## Tips for Physical Pentesting

- **Digital signage**: Most commercial displays use Samsung/LG protocols — power off or change input
- **Conference rooms**: Projectors typically use NEC protocol — power cycle during meetings
- **Hotel TVs**: Often Samsung or LG with standard IR — full remote control
- **Retail**: Point-of-sale displays can often be powered off
- **Security cameras**: Some older IP cameras have IR-controlled settings menus

---

**FLLC 2026** — For authorized physical security testing only.
