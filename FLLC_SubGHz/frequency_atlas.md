# FLLC Sub-GHz Frequency Atlas

> Complete reference for Sub-GHz radio frequencies relevant to security research.
> FLLC 2026 — FU PERSON

---

## ISM Band Allocations

| Region | Frequency Range | Common Uses |
|--------|----------------|-------------|
| Worldwide | 433.05–434.79 MHz | IoT sensors, weather stations, car key fobs |
| Americas | 315 MHz | Garage doors, car remotes (older US vehicles) |
| Americas | 902–928 MHz | LoRa, Z-Wave, smart home, industrial IoT |
| Europe | 868–870 MHz | LoRa, SRD, alarm systems, smart meters |
| Japan | 920–928 MHz | Wi-SUN, LPWA |
| China | 470–510 MHz | LPWAN, metering |

---

## Common Protocols & Frequencies

### Garage Doors / Gates
| Protocol | Frequency | Modulation | Notes |
|----------|-----------|------------|-------|
| Fixed Code | 300/310/315/390 MHz | OOK/ASK | Easily captured and replayed |
| Linear/MegaCode | 318 MHz | OOK | 24-bit fixed code |
| Chamberlain/LiftMaster | 315/390 MHz | Rolling code | Security+ 2.0, cannot replay |
| CAME | 433.92 MHz | OOK | 12-bit fixed code (EU) |
| Nice FLO/FLOR | 433.92 MHz | OOK/Rolling | Fixed (FLO) and rolling (FLOR) variants |
| BFT | 433.92 MHz | OOK | Fixed code, some rolling |
| Hormann | 868.3 MHz | BiSecur | Rolling code, encrypted |

### Car Key Fobs
| Region | Frequency | Protocol | Security |
|--------|-----------|----------|----------|
| North America | 315 MHz | Varies | Mix of fixed and rolling |
| Europe | 433.92 MHz | Varies | Rolling code standard |
| Japan | 315 MHz | Varies | Rolling code standard |

### Smart Home / IoT
| Device Type | Frequency | Protocol |
|-------------|-----------|----------|
| Z-Wave | 908.42 MHz (US) / 868.42 MHz (EU) | Z-Wave Plus |
| LoRa | 915 MHz (US) / 868 MHz (EU) | LoRaWAN |
| Zigbee | 2.4 GHz (not Sub-GHz) | IEEE 802.15.4 |
| Thread | 2.4 GHz (not Sub-GHz) | IEEE 802.15.4 |
| Oregon Scientific | 433.92 MHz | OOK | Weather stations |
| Honeywell | 345 MHz | OOK/FSK | Security sensors |
| 2GIG | 345 MHz | OOK | Security panels |
| DSC | 433 MHz | OOK | Security sensors |

### TPMS (Tire Pressure Monitoring)
| Region | Frequency | Modulation |
|--------|-----------|------------|
| North America | 315 MHz | FSK/OOK |
| Europe | 433.92 MHz | FSK/OOK |

### Pagers
| Service | Frequency | Protocol |
|---------|-----------|----------|
| POCSAG | 152–170 MHz | FSK |
| FLEX | 929–932 MHz | 4-level FSK |

---

## Modulation Types

| Type | Full Name | Description |
|------|-----------|-------------|
| OOK | On-Off Keying | Simplest AM — carrier on/off. Most garage doors. |
| ASK | Amplitude Shift Keying | Carrier amplitude varies. Similar to OOK. |
| FSK | Frequency Shift Keying | Frequency shifts between two values. More noise-resistant. |
| GFSK | Gaussian FSK | Smoothed FSK transitions. Used in Bluetooth, some IoT. |
| LoRa | Long Range | Chirp spread spectrum. Very long range, low power. |

---

## Flipper Zero Sub-GHz Capabilities

| Feature | Status |
|---------|--------|
| Frequency range | 300–348 MHz, 387–464 MHz, 779–928 MHz |
| RX (receive) | All supported frequencies |
| TX (transmit) | Region-locked by firmware (unlocked in custom FW) |
| Modulation | AM270, AM650, FM238, FM476 |
| Raw capture | Yes — captures raw signal for analysis |
| Protocol decode | 40+ protocols built-in |
| Replay | Yes — for fixed code signals |
| Brute force | Yes — for short code lengths |
| Frequency analyzer | Built-in spectrum analyzer |

---

## Legal Notice

Sub-GHz transmission is regulated by your local authority (FCC, ETSI, ARIB, etc.).
Unauthorized transmission on certain frequencies is illegal. This reference is for
authorized security research and educational purposes only.

**FLLC 2026** — FU PERSON by PERSON FU
