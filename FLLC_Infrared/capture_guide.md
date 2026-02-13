# FLLC Infrared Capture & Replay Guide

> Step-by-step guide for capturing, analyzing, and replaying IR signals.
> FLLC 2026 — FU PERSON

---

## Equipment

| Item | Purpose |
|------|---------|
| Flipper Zero | Capture, store, and replay IR signals |
| Original remote | Source of IR signals to clone |
| IR LED array (optional) | Boost replay range beyond Flipper's built-in LED |

---

## Step 1: Identify the Target

Before capturing, identify what you're targeting:
- **Brand and model** of the device
- **Existing remote** — borrow it temporarily
- **Protocol** — check the universal codes reference first

---

## Step 2: Capture with Flipper Zero

### Known Protocol (Parsed)
1. Navigate: **Infrared -> Learn New Remote**
2. Name the remote (e.g., "Samsung_TV_Office")
3. Point the original remote at Flipper's IR receiver (top of device)
4. Press each button on the original remote, one at a time
5. Name each button (Power, Vol+, Vol-, Mute, Input, etc.)
6. Flipper decodes: protocol, address, command
7. Save to SD card

### Unknown Protocol (Raw)
1. Navigate: **Infrared -> Learn New Signal**
2. Point remote at Flipper
3. Press button
4. If Flipper says "Unknown" — it saves raw timing data
5. Raw signals can be replayed but not edited easily

---

## Step 3: Organize on SD Card

IR files are stored in `/infrared/` on the SD card:

```
/ext/infrared/
  Samsung_TV_Office.ir
  LG_Lobby_Display.ir
  Epson_Projector_CR3.ir
  AC_Server_Room.ir
```

---

## Step 4: Replay

1. **Infrared -> Saved Remotes**
2. Select the remote file
3. Select the button to send
4. Point Flipper at the target device (within 3-5 meters)
5. Press **Send**

### Boost Range
The Flipper's built-in IR LED has ~3-5m range. To increase:
- Use an external IR LED array connected to GPIO
- Or use the Flipper IR board accessory
- Line-of-sight is critical — IR does not go through walls

---

## Step 5: Analyze Signals

### Using Flipper
- View saved signals: shows protocol, address, command
- Compare signals: same protocol = same manufacturer
- Raw view: shows pulse/space timing in microseconds

### Using External Tools
- **IrScrutinizer**: Desktop tool for IR signal analysis
- **LIRC**: Linux Infrared Remote Control database
- **IRremote** (Arduino): Decode and send IR from microcontrollers

---

## Advanced: Creating Custom IR Files

You can manually create `.ir` files:

```
Filetype: IR signals file
Version: 1
#
# FLLC Custom IR File
#
name: Power
type: parsed
protocol: NEC
address: 04 00 00 00
command: 08 00 00 00
#
name: Volume_Up
type: parsed
protocol: NEC
address: 04 00 00 00
command: 02 00 00 00
#
name: Raw_Signal
type: raw
frequency: 38000
duty_cycle: 0.330000
data: 9024 4512 564 564 564 1692 564 564 564 564
```

---

## Protocol Quick Reference

| Protocol | Carrier | Bits | Timing |
|----------|---------|------|--------|
| NEC | 38 kHz | 32 | 9ms leader, 562us bit |
| RC5 | 36 kHz | 14 | Manchester encoded |
| RC6 | 36 kHz | 20+ | Manchester with leader |
| SIRC (Sony) | 40 kHz | 12/15/20 | 2.4ms leader |
| Samsung | 38 kHz | 32 | 4.5ms leader |
| Sharp | 38 kHz | 48 | Expansion bit protocol |

---

**FLLC 2026** — For authorized security research only.
