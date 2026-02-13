# Rolling Code Attacks — Theory & Countermeasures

> FLLC 2026 — Educational reference for security researchers.

---

## How Rolling Codes Work

Rolling codes (also called hopping codes) are a security mechanism used in keyless entry systems:

1. **Transmitter** (key fob) and **Receiver** (car/garage) share a secret seed and counter
2. Each button press generates a new code using a PRNG seeded with the shared secret
3. The receiver maintains a window of valid future codes (typically 256 ahead)
4. Once a code is used, all previous codes are invalidated
5. Protocols: KeeLoq, AUT64, Security+ 2.0, Hitag2

---

## RollJam Attack (Samy Kamkar, 2015)

### Concept
1. Victim presses key fob button
2. Attacker **jams** the receiver while **capturing** the rolling code
3. Victim presses again (thinking first press failed)
4. Attacker **jams** the second code, **replays** the first code to open
5. Attacker now holds one valid unused code for later use

### Requirements
- Two radios: one to jam, one to capture
- Precise timing to jam the receiver but still capture the signal
- The captured code remains valid until the victim presses the button again

### Why It Works
- The receiver only invalidates codes it has **seen**
- An unseen code within the valid window remains usable
- The jammer prevents the receiver from seeing the real transmission

---

## RollBack Attack (2022)

### Concept
- Exploits vulnerability in Honda, Toyota, and other implementations
- The counter can be **reset** by sending a specific sequence
- After reset, previously captured codes become valid again

### Affected Systems
- Honda Civic, CR-V, Accord (2012–2022 models with weak KeeLoq implementation)
- Some Toyota and Hyundai models

---

## KeeLoq Cryptanalysis

| Attack | Type | Complexity | Practical? |
|--------|------|-----------|------------|
| Slide attack | Algebraic | 2^16 known plaintexts | Yes |
| Side-channel | Power analysis | Physical access to receiver | Yes |
| Brute force | Key space | 2^64 operations | Not practical |
| Correlation attack | Statistical | 2^26 chosen plaintexts | Research only |

---

## Countermeasures

| Defense | Description |
|---------|-------------|
| **Dual-frequency** | TX on two frequencies simultaneously — harder to jam both |
| **Time-based validation** | Reject codes that arrive too late after generation |
| **Challenge-response** | Require bidirectional communication (UWB, BLE) |
| **UWB ranging** | Ultra-wideband distance measurement prevents relay attacks |
| **Anomaly detection** | Detect jamming patterns and alert the user |
| **Faraday pouch** | Physical: store key fob in signal-blocking pouch |

---

## Flipper Zero Limitations

The Flipper Zero **cannot** break rolling codes by itself:
- It can capture rolling code signals but cannot replay them (the code is already consumed)
- The RollJam attack requires **two simultaneous radios** (one jam, one capture)
- The Flipper has only **one radio** — it cannot jam and capture at the same time
- Custom firmware does not change this hardware limitation

What the Flipper **can** do:
- Capture and replay **fixed code** signals (older systems)
- Analyze rolling code signals to identify the protocol
- Act as one half of a two-device RollJam setup (with external jammer)

---

**FLLC 2026** — For authorized security research only.
