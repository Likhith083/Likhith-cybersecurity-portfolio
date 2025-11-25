#!/usr/bin/env python3
"""
Script to update an allow-list file by removing IPs listed in a remove file.

Usage:
  python update_allow_list.py --allow-file allow_list.txt --remove-file remove_list.txt [--dry-run] [--no-backup]

This script:
 - reads the allow list file into a cleaned list of IPs
 - reads the remove list file into a cleaned list of IPs
 - removes any matching IPs from the allow list
 - optionally writes changes back to the allow list (with an automatic backup)

The script tolerates blank lines and `#` comments in the input files.
"""
from __future__ import annotations

import argparse
import datetime
import ipaddress
import shutil
import sys
from pathlib import Path
from typing import List, Tuple


def read_list(path: Path) -> List[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    lines = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        lines.append(s)
    return lines


def write_list(path: Path, items: List[str]) -> None:
    # ensure newline-terminated file
    content = "\n".join(items) + ("\n" if items else "")
    path.write_text(content, encoding="utf-8")


def safe_validate_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def backup_file(path: Path) -> Path:
    ts = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    bak = path.with_name(f"{path.name}.{ts}.bak")
    shutil.copy2(path, bak)
    return bak


def update_allow_list(allow_file: Path, remove_ips: List[str], dry_run: bool = True, backup: bool = True) -> Tuple[List[str], List[str]]:
    """Update the allow list file by removing the entries in remove_ips.

    Returns a tuple (removed, remaining).
    """
    allow_ips = read_list(allow_file)
    # normalize: remove duplicates while preserving order
    seen = set()
    normalized = []
    for ip in allow_ips:
        if ip in seen:
            continue
        seen.add(ip)
        normalized.append(ip)
    allow_ips = normalized

    # filter remove list: strip and ignore blanks/comments
    to_remove = [r.strip() for r in remove_ips if r.strip() and not r.strip().startswith("#")]

    removed = [ip for ip in allow_ips if ip in to_remove]
    remaining = [ip for ip in allow_ips if ip not in to_remove]

    if dry_run:
        return removed, remaining

    # perform backup and write
    if backup and allow_file.exists():
        bak = backup_file(allow_file)
        print(f"Backed up '{allow_file}' to '{bak}'")

    write_list(allow_file, remaining)
    return removed, remaining


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Update allow list by removing IPs from a remove list.")
    p.add_argument("--allow-file", "-a", default="allow_list.txt", help="Path to allow list file")
    p.add_argument("--remove-file", "-r", default="remove_list.txt", help="Path to remove list file")
    p.add_argument("--dry-run", action="store_true", help="Show what would be removed without modifying files")
    p.add_argument("--no-backup", dest="backup", action="store_false", help="Do not create a backup before writing")
    return p.parse_args()


def main(argv: List[str] | None = None) -> int:
    args = _parse_args() if argv is None else _parse_args()
    allow_path = Path(args.allow_file)
    remove_path = Path(args.remove_file)

    remove_ips = read_list(remove_path)

    removed, remaining = update_allow_list(allow_path, remove_ips, dry_run=args.dry_run, backup=args.backup)

    if removed:
        print("Removed entries:")
        for ip in removed:
            valid = "(valid)" if safe_validate_ip(ip) else "(invalid)"
            print(f"  {ip} {valid}")
    else:
        print("No matching IPs found to remove.")

    print(f"Remaining entries: {len(remaining)}")
    if args.dry_run:
        print("Dry-run mode; no files were changed.")
    else:
        print(f"Wrote updated allow list to '{allow_path}'")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
