#!/usr/bin/env python3
"""
strength_audit.py
-----------------
Audits password strength the way a security-aware tool should: not just
"does it have a number and a symbol", but how long it would actually take
an attacker to crack it, and whether it's a known-weak/common password.

Checks performed per password:
  1. Common-password / wordlist match  (instant crack -> critical fail)
  2. Length and character-set variety  (determines brute-force keyspace)
  3. Estimated entropy (bits)
  4. Estimated crack time at 3 attack speeds:
       - online, rate-limited login        (~10 guesses/sec)
       - offline, fast hash e.g. MD5/SHA1 on a GPU (~10 billion guesses/sec)
       - offline, slow hash e.g. bcrypt/sha512crypt (~10,000 guesses/sec)
  5. Simple pattern checks (keyboard walk, repeated chars, all-digits, etc.)

Usage:
    python3 strength_audit.py "MyP@ssw0rd123"
    python3 strength_audit.py --file passwords.txt
    python3 strength_audit.py            # interactive prompt
"""

import argparse
import getpass
import math
import re
import sys
import os

COMMON_LIST_PATH = os.path.join(os.path.dirname(__file__), "..", "wordlists", "common.txt")

KEYBOARD_ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]

GUESS_RATES = {
    "Online login (rate-limited, ~10/sec)": 10,
    "Offline fast hash - MD5/SHA1 on GPU (~1e10/sec)": 10_000_000_000,
    "Offline slow hash - bcrypt/sha512crypt (~1e4/sec)": 10_000,
}


def load_common_passwords():
    try:
        with open(COMMON_LIST_PATH) as f:
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        return set()


def charset_size(password: str) -> int:
    size = 0
    if re.search(r"[a-z]", password):
        size += 26
    if re.search(r"[A-Z]", password):
        size += 26
    if re.search(r"[0-9]", password):
        size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        size += 33  # common printable symbols
    return size or 1


def entropy_bits(password: str) -> float:
    pool = charset_size(password)
    return len(password) * math.log2(pool)


def has_keyboard_walk(password: str, min_run=4) -> bool:
    lower = password.lower()
    for row in KEYBOARD_ROWS:
        for i in range(len(row) - min_run + 1):
            run = row[i:i + min_run]
            if run in lower or run[::-1] in lower:
                return True
    return False


def has_repeated_chars(password: str, min_run=4) -> bool:
    return bool(re.search(r"(.)\1{" + str(min_run - 1) + ",}", password))


def human_time(seconds: float) -> str:
    units = [
        ("centuries", 100 * 365 * 24 * 3600),
        ("years", 365 * 24 * 3600),
        ("days", 24 * 3600),
        ("hours", 3600),
        ("minutes", 60),
        ("seconds", 1),
    ]
    if seconds < 1:
        return "instantly"
    for name, size in units:
        if seconds >= size:
            value = seconds / size
            if name == "centuries" and value > 1_000_000:
                return "longer than the age of the universe"
            return f"{value:,.1f} {name}"
    return "instantly"


def audit(password: str, common_passwords: set) -> dict:
    issues = []
    lower = password.lower()

    is_common = lower in common_passwords
    if is_common:
        issues.append("Exact match in common-password list -> cracked in under 1 second by any tool")

    if len(password) < 8:
        issues.append(f"Too short ({len(password)} chars) -> use at least 12")
    if password.isdigit():
        issues.append("All digits -> trivial brute force")
    if password.isalpha() and password.islower():
        issues.append("All lowercase letters -> weak character variety")
    if has_keyboard_walk(password):
        issues.append("Contains a keyboard-walk pattern (e.g. 'qwerty', 'asdf')")
    if has_repeated_chars(password):
        issues.append("Contains 4+ repeated characters in a row")
    if re.search(r"(19|20)\d{2}$", password):
        issues.append("Ends in what looks like a year -> common and guessable")

    bits = entropy_bits(password)
    crack_times = {
        label: (float("inf") if is_common else (2 ** bits) / 2 / rate)
        for label, rate in GUESS_RATES.items()
    }

    if is_common:
        verdict = "CRITICAL - known password, cracked instantly"
    elif bits < 28:
        verdict = "VERY WEAK"
    elif bits < 40:
        verdict = "WEAK"
    elif bits < 60:
        verdict = "MODERATE"
    elif bits < 80:
        verdict = "STRONG"
    else:
        verdict = "VERY STRONG"

    return {
        "password": password,
        "length": len(password),
        "charset_size": charset_size(password),
        "entropy_bits": bits,
        "is_common": is_common,
        "issues": issues,
        "verdict": verdict,
        "crack_times": crack_times,
    }


def print_report(result: dict):
    masked = result["password"][0] + "*" * (len(result["password"]) - 1) if result["password"] else ""
    print(f"\n{'='*60}")
    print(f"Password: {masked}  (length {result['length']})")
    print(f"Verdict:  {result['verdict']}")
    print(f"Entropy:  {result['entropy_bits']:.1f} bits  (charset size ~{result['charset_size']})")

    if result["issues"]:
        print("Issues found:")
        for issue in result["issues"]:
            print(f"  - {issue}")
    else:
        print("No obvious pattern issues found.")

    print("Estimated time to crack:")
    for label, seconds in result["crack_times"].items():
        t = "instantly (known password)" if math.isinf(seconds) else human_time(seconds)
        print(f"  {label:50s} {t}")
    print(f"{'='*60}")


def main():
    p = argparse.ArgumentParser(description="Password strength auditor")
    p.add_argument("password", nargs="?", help="password to audit")
    p.add_argument("--file", help="file of passwords, one per line")
    args = p.parse_args()

    common = load_common_passwords()

    if args.file:
        with open(args.file) as f:
            for line in f:
                pw = line.strip()
                if pw:
                    print_report(audit(pw, common))
    elif args.password:
        print_report(audit(args.password, common))
    else:
        pw = getpass.getpass("Enter password to audit (hidden input): ")
        print_report(audit(pw, common))


if __name__ == "__main__":
    main()
