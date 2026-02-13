#!/usr/bin/env python3
"""
FLLC Flipper Zero SD Card Organizer
====================================
Validates, organizes, and optimizes the Flipper Zero SD card structure.
Ensures all required directories exist, removes duplicates, and generates
an inventory report.

FLLC 2026 — FU PERSON by PERSON FU
"""

import os
import sys
import hashlib
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Standard Flipper Zero SD card directory structure
FLIPPER_DIRS = [
    "badusb",
    "dolphin",
    "infrared",
    "infrared/assets",
    "ibutton",
    "lfrfid",
    "nfc",
    "nfc/assets",
    "subghz",
    "subghz/assets",
    "music_player",
    "wav_player",
    "apps",
    "apps_data",
    "u2f",
    "picopass",
    "update",
    # FLLC custom directories
    "fllc",
    "fllc/badusb",
    "fllc/subghz",
    "fllc/nfc",
    "fllc/infrared",
    "fllc/tools",
    "fllc/loot",
    "fllc/logs",
]

# File extension to directory mapping
EXT_MAP = {
    ".sub": "subghz",
    ".ir": "infrared",
    ".nfc": "nfc",
    ".rfid": "lfrfid",
    ".ibtn": "ibutton",
    ".txt": "badusb",  # BadUSB scripts
    ".fap": "apps",
    ".wav": "wav_player",
    ".fmf": "music_player",
    ".picopass": "picopass",
    ".u2f": "u2f",
}


def sha256_file(filepath):
    """Calculate SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_directories(sd_root):
    """Create all required Flipper directories."""
    created = []
    for d in FLIPPER_DIRS:
        full = os.path.join(sd_root, d)
        if not os.path.exists(full):
            os.makedirs(full, exist_ok=True)
            created.append(d)
    return created


def find_duplicates(sd_root):
    """Find duplicate files by hash."""
    hash_map = defaultdict(list)
    for root, dirs, files in os.walk(sd_root):
        # Skip hidden and system directories
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.startswith("."):
                continue
            fp = os.path.join(root, f)
            try:
                h = sha256_file(fp)
                rel = os.path.relpath(fp, sd_root)
                hash_map[h].append(rel)
            except (PermissionError, OSError):
                pass

    return {h: paths for h, paths in hash_map.items() if len(paths) > 1}


def organize_loose_files(sd_root):
    """Move files from root to appropriate directories based on extension."""
    moved = []
    for item in os.listdir(sd_root):
        fp = os.path.join(sd_root, item)
        if not os.path.isfile(fp):
            continue
        ext = os.path.splitext(item)[1].lower()
        if ext in EXT_MAP:
            dest_dir = os.path.join(sd_root, EXT_MAP[ext])
            os.makedirs(dest_dir, exist_ok=True)
            dest = os.path.join(dest_dir, item)
            if not os.path.exists(dest):
                shutil.move(fp, dest)
                moved.append(f"{item} -> {EXT_MAP[ext]}/")
    return moved


def generate_inventory(sd_root):
    """Generate a complete inventory of the SD card."""
    inventory = {
        "generated": datetime.now().isoformat(),
        "root": sd_root,
        "directories": {},
        "total_files": 0,
        "total_size_bytes": 0,
    }

    for root, dirs, files in os.walk(sd_root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        rel_dir = os.path.relpath(root, sd_root)
        if rel_dir == ".":
            rel_dir = "/"

        dir_files = []
        for f in files:
            if f.startswith("."):
                continue
            fp = os.path.join(root, f)
            try:
                size = os.path.getsize(fp)
                dir_files.append({"name": f, "size": size})
                inventory["total_files"] += 1
                inventory["total_size_bytes"] += size
            except OSError:
                pass

        if dir_files:
            inventory["directories"][rel_dir] = dir_files

    return inventory


def main():
    if len(sys.argv) < 2:
        print("=" * 50)
        print("  FLLC Flipper Zero SD Organizer v2026")
        print("=" * 50)
        print()
        print("Usage: python sd_organizer.py <sd_card_path> [options]")
        print()
        print("Options:")
        print("  --organize    Move loose files to correct directories")
        print("  --dedup       Find and report duplicate files")
        print("  --inventory   Generate full SD card inventory (JSON)")
        print("  --all         Run all operations")
        print()
        print("Example:")
        print("  python sd_organizer.py E:\\ --all")
        return

    sd_root = sys.argv[1]
    options = set(sys.argv[2:])

    if not os.path.isdir(sd_root):
        print(f"[!] Path not found: {sd_root}")
        return

    run_all = "--all" in options

    print("=" * 50)
    print("  FLLC Flipper Zero SD Organizer v2026")
    print(f"  Target: {sd_root}")
    print("=" * 50)

    # Always ensure directories exist
    print("\n[*] Ensuring directory structure...")
    created = ensure_directories(sd_root)
    if created:
        print(f"    Created {len(created)} directories:")
        for d in created:
            print(f"      + {d}/")
    else:
        print("    All directories present.")

    if "--organize" in options or run_all:
        print("\n[*] Organizing loose files...")
        moved = organize_loose_files(sd_root)
        if moved:
            print(f"    Moved {len(moved)} files:")
            for m in moved:
                print(f"      > {m}")
        else:
            print("    No loose files to organize.")

    if "--dedup" in options or run_all:
        print("\n[*] Scanning for duplicates...")
        dupes = find_duplicates(sd_root)
        if dupes:
            print(f"    Found {len(dupes)} duplicate groups:")
            for h, paths in dupes.items():
                print(f"    Hash: {h[:16]}...")
                for p in paths:
                    print(f"      - {p}")
        else:
            print("    No duplicates found.")

    if "--inventory" in options or run_all:
        print("\n[*] Generating inventory...")
        inv = generate_inventory(sd_root)
        inv_path = os.path.join(sd_root, "fllc", "inventory.json")
        with open(inv_path, "w") as f:
            json.dump(inv, f, indent=2)
        size_mb = inv["total_size_bytes"] / (1024 * 1024)
        print(f"    Files: {inv['total_files']} | Size: {size_mb:.1f} MB")
        print(f"    Saved: {inv_path}")

    print("\n[+] Done.")


if __name__ == "__main__":
    main()
