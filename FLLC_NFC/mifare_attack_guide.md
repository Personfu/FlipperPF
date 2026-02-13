# FLLC NFC Attack Guide — Mifare, NDEF, EMV

> Comprehensive NFC security research reference.
> FLLC 2026 — FU PERSON

---

## Mifare Classic Vulnerabilities

### Architecture
- 1K: 16 sectors, 4 blocks each (64 bytes/sector, 1024 bytes total)
- 4K: 40 sectors (32x4 blocks + 8x16 blocks, 4096 bytes total)
- Each sector protected by two keys: Key A and Key B
- Authentication uses proprietary CRYPTO1 cipher (broken since 2008)

### Known Attacks

| Attack | Description | Tool |
|--------|-------------|------|
| **Default Keys** | Many cards ship with well-known keys (FFFFFFFFFFFF, A0A1A2A3A4A5, etc.) | Flipper, Proxmark3 |
| **Nested Attack** | If one key is known, derive other sector keys via CRYPTO1 weakness | mfoc, Flipper |
| **Darkside Attack** | Recover a key with NO prior knowledge (exploits PRNG weakness) | mfcuk, Proxmark3 |
| **Hardnested** | Attacks Mifare Classic EV1 (improved PRNG) — still broken | Proxmark3 |
| **Relay Attack** | Relay NFC communication between card and reader over distance | NFCGate |
| **Brute Force** | Try all possible keys (2^48, impractical without optimization) | Not practical |

### Default Key Dictionary
```
FFFFFFFFFFFF
A0A1A2A3A4A5
D3F7D3F7D3F7
000000000000
B0B1B2B3B4B5
4D3A99C351DD
1A982C7E459A
AABBCCDDEEFF
714C5C886E97
587EE5F9350F
A0478CC39091
533CB6C723F6
8FD0A4F256E9
```

### Flipper Zero NFC Capabilities
| Feature | Status |
|---------|--------|
| Read UID | Yes — all Mifare types |
| Read full dump | Yes — if keys are known |
| Dictionary attack | Yes — built-in key dictionary |
| Nested attack | Yes (with Unleashed/Momentum firmware) |
| Emulate card | Yes — full Mifare Classic emulation |
| Write to card | Yes — clone to magic card (Gen1a, Gen2) |
| Darkside attack | Limited (Proxmark3 recommended) |

---

## NDEF (NFC Data Exchange Format)

### What Is NDEF?
NDEF is the standard format for storing data on NFC tags. When a phone taps an NFC tag, NDEF records tell the phone what to do.

### Attack Vectors
| Attack | Description |
|--------|-------------|
| **URL Redirect** | Tag opens a phishing URL automatically |
| **WiFi Provisioning** | Tag auto-connects phone to attacker's WiFi |
| **App Launch** | Tag opens a specific app (Android) |
| **vCard Injection** | Tag adds a contact with attacker's info |
| **Phone Call** | Tag initiates a phone call to a premium number |
| **SMS** | Tag sends an SMS message |

### Social Engineering Applications
1. Place tag under a "Free WiFi" sticker — auto-connects to evil twin AP
2. Place tag on a "Scan for menu" sign — redirects to credential harvesting page
3. Encode vCard with spoofed identity — victim adds to contacts
4. Tag behind a poster — phone opens malicious APK download

---

## EMV Contactless

### What Can Be Read?
When you tap a contactless payment card:
- PAN (card number) — in the clear
- Expiration date — in the clear
- Cardholder name — sometimes
- Transaction history — sometimes (limited)

### What CANNOT Be Read?
- CVV/CVC (the 3-digit code on the back)
- iCVV (dynamic cryptographic verification value)
- PIN

### Why Skimming Is Limited
- EMV generates a unique cryptogram per transaction
- Without the card's private key, you cannot create valid transactions
- The iCVV is different from the magnetic stripe CVV
- Online transactions require CVV which is NOT on the chip

---

## Magic Cards Reference

| Type | UID Writable | Block 0 Writable | Compatible With |
|------|-------------|-------------------|-----------------|
| Gen1a (UID) | Yes | Yes (special command) | Most readers |
| Gen2 (CUID) | Yes | Yes (standard write) | More compatible |
| Gen3 (UFUID) | Once | Once (then locks) | Most secure clone |
| Gen4 (GTU) | Yes | Yes | Ultimate compatibility |

---

**FLLC 2026** — For authorized security research only.
