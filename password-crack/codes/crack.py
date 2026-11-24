#!/usr/bin/env python3
"""
crack.py
--------
A from-scratch password cracker. This is literally what John the Ripper and
Hashcat do under the hood for a CPU dictionary/brute-force attack:

    for each candidate password:
        hash(candidate)
        if hash(candidate) == target_hash:
            found it

The point of writing this yourself is to understand *why* cracking works
(and why it's fast or slow), before you let a real tool like John/Hashcat
do it with GPU speed and smarter rules.

Usage:
    python3 crack.py --mode dict  --algo md5    --hashfile ../hashes/md5.txt
    python3 crack.py --mode brute --algo sha1    --hashfile ../hashes/sha1.txt --maxlen 4
    python3 crack.py --mode dict  --algo sha512crypt --hashfile ../hashes/shadow_like.txt
"""

import argparse
import hashlib
import itertools
import string
import sys
import time

try:
    from passlib.hash import sha512_crypt
    HAVE_PASSLIB = True
except ImportError:
    HAVE_PASSLIB = False


def hash_candidate(candidate: str, algo: str, sample_hash: str = "") -> str:
    data = candidate.encode()
    if algo == "md5":
        return hashlib.md5(data).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(data).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(data).hexdigest()
    elif algo == "sha512crypt":
        if not HAVE_PASSLIB:
            sys.exit("[-] Need 'passlib' for sha512crypt: pip install passlib")
        # sha512crypt hashes are salted AND carry their own round count
        # ($6$rounds=N$salt$hash). We must reuse BOTH the salt and the round
        # count from the target hash, or we'll never match it -- and if we
        # forget the rounds, passlib silently falls back to its (very high,
        # very slow) default round count instead of erroring.
        parsed = sha512_crypt.from_string(sample_hash)
        return sha512_crypt.using(salt=parsed.salt, rounds=parsed.rounds).hash(candidate)
    else:
        sys.exit(f"[-] Unknown algo: {algo}")


def load_targets(path: str):
    """Returns list of (user, hash) tuples."""
    targets = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            user, h = line.split(":", 1)
            targets.append((user, h))
    return targets


def dictionary_attack(targets, algo, wordlist_path):
    remaining = dict(targets)  # hash -> user, we'll pop as we crack
    by_hash = {h: u for u, h in targets}
    cracked = {}

    with open(wordlist_path, errors="ignore") as wl:
        words = [w.strip() for w in wl if w.strip()]

    print(f"[*] Loaded {len(words)} candidate words, {len(targets)} target hash(es)")
    start = time.time()
    tried = 0

    for word in words:
        if not by_hash:
            break
        for candidate in (word, word.lower(), word.capitalize(), word.upper()):
            tried += 1
            for target_hash, user in list(by_hash.items()):
                guess_hash = hash_candidate(candidate, algo, sample_hash=target_hash)
                if guess_hash == target_hash:
                    cracked[user] = candidate
                    print(f"[+] CRACKED {user:8s} -> '{candidate}'  ({tried} guesses so far)")
                    del by_hash[target_hash]

    elapsed = time.time() - start
    print(f"\n[*] Dictionary attack done: {len(cracked)}/{len(targets)} cracked "
          f"in {elapsed:.2f}s ({tried} guesses, {tried/elapsed:.0f} guesses/sec)")
    for user, h in targets:
        if user not in cracked:
            print(f"[-] NOT cracked: {user} (hash: {h[:20]}...)")
    return cracked


def brute_force_attack(targets, algo, maxlen, charset):
    by_hash = {h: u for u, h in targets}
    cracked = {}
    start = time.time()
    tried = 0

    for length in range(1, maxlen + 1):
        if not by_hash:
            break
        print(f"[*] Trying all {length}-character combinations "
              f"({len(charset)}^{length} = {len(charset)**length:,} guesses)...")
        for combo in itertools.product(charset, repeat=length):
            if not by_hash:
                break
            candidate = "".join(combo)
            tried += 1
            for target_hash, user in list(by_hash.items()):
                guess_hash = hash_candidate(candidate, algo, sample_hash=target_hash)
                if guess_hash == target_hash:
                    cracked[user] = candidate
                    print(f"[+] CRACKED {user:8s} -> '{candidate}'  ({tried} guesses so far)")
                    del by_hash[target_hash]

    elapsed = time.time() - start
    print(f"\n[*] Brute-force done: {len(cracked)} cracked "
          f"in {elapsed:.2f}s ({tried} guesses, {tried/elapsed:.0f} guesses/sec)")
    for user, h in targets:
        if user not in cracked:
            print(f"[-] NOT cracked: {user} (too long/complex for maxlen={maxlen})")
    return cracked


def main():
    p = argparse.ArgumentParser(description="Educational password cracker")
    p.add_argument("--mode", choices=["dict", "brute"], required=True)
    p.add_argument("--algo", choices=["md5", "sha1", "sha256", "sha512crypt"], required=True)
    p.add_argument("--hashfile", required=True, help="path to user:hash file")
    p.add_argument("--wordlist", default="../wordlists/common.txt")
    p.add_argument("--maxlen", type=int, default=4, help="brute-force max password length")
    p.add_argument("--charset", default=string.ascii_lowercase + string.digits,
                    help="brute-force character set")
    args = p.parse_args()

    targets = load_targets(args.hashfile)
    if not targets:
        sys.exit(f"[-] No targets loaded from {args.hashfile}")

    if args.mode == "dict":
        dictionary_attack(targets, args.algo, args.wordlist)
    else:
        brute_force_attack(targets, args.algo, args.maxlen, args.charset)


if __name__ == "__main__":
    main()
