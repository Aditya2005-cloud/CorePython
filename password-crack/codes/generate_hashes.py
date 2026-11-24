#!/usr/bin/env python3
"""
generate_hashes.py
------------------
Creates a fake "leaked password database" so you have something legal and
safe to crack. Every password here is intentionally weak and comes straight
from the wordlist (plus a couple of "harder" ones that aren't in it), so you
can see both the success case and the failure case when cracking.

Writes:
  hashes/md5.txt      -> user:hash          (crackable with John: --format=raw-md5)
  hashes/sha1.txt      -> user:hash          (crackable with John: --format=raw-sha1)
  hashes/sha256.txt    -> user:hash          (crackable with John: --format=raw-sha256)
  hashes/shadow_like.txt -> user:$6$salt$hash  (sha512crypt, like a real /etc/shadow line)
"""

import hashlib
import os
import random
import string
from passlib.hash import sha512_crypt

HASH_DIR = os.path.join(os.path.dirname(__file__), "..", "hashes")

USERS_AND_PASSWORDS = {
    "alice":   "password",        # in wordlist -> will crack instantly
    "bob":     "dragon",          # in wordlist
    "carol":   "Summer2024!",     # NOT in wordlist, NOT in brute-force range -> will fail (on purpose)
    "dave":    "qwerty",          # in wordlist
    "eve":     "p@ssw0rd",        # NOT in wordlist -> good example of a "looks strong, isn't" password
    "frank":   "ab12",            # short -> crackable by brute force even though not in the wordlist
}


def random_salt(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def main():
    md5_lines, sha1_lines, sha256_lines, shadow_lines = [], [], [], []

    for user, pwd in USERS_AND_PASSWORDS.items():
        pwd_bytes = pwd.encode()

        md5_lines.append(f"{user}:{hashlib.md5(pwd_bytes).hexdigest()}")
        sha1_lines.append(f"{user}:{hashlib.sha1(pwd_bytes).hexdigest()}")
        sha256_lines.append(f"{user}:{hashlib.sha256(pwd_bytes).hexdigest()}")

        # sha512crypt ($6$...) is what modern Linux /etc/shadow actually uses.
        # Real /etc/shadow uses ~656,000 rounds by default, which is so slow
        # that a pure-Python cracker trying even a 41-word list takes minutes.
        # We use a much lower round count here purely so this demo finishes
        # in seconds -- it's still the same algorithm, just not realistically
        # tuned. Real John/Hashcat would use the full round count and rely on
        # heavy optimization + GPUs to still be fast.
        shadow_hash = sha512_crypt.using(rounds=5000).hash(pwd)
        shadow_lines.append(f"{user}:{shadow_hash}")

    os.makedirs(HASH_DIR, exist_ok=True)
    with open(os.path.join(HASH_DIR, "md5.txt"), "w") as f:
        f.write("\n".join(md5_lines) + "\n")
    with open(os.path.join(HASH_DIR, "sha1.txt"), "w") as f:
        f.write("\n".join(sha1_lines) + "\n")
    with open(os.path.join(HASH_DIR, "sha256.txt"), "w") as f:
        f.write("\n".join(sha256_lines) + "\n")
    with open(os.path.join(HASH_DIR, "shadow_like.txt"), "w") as f:
        f.write("\n".join(shadow_lines) + "\n")

    print("[+] Wrote hashes/md5.txt, sha1.txt, sha256.txt, shadow_like.txt")
    print("[+] Answer key (so you can check your cracker's results):")
    for user, pwd in USERS_AND_PASSWORDS.items():
        print(f"    {user:6s} -> {pwd}")


if __name__ == "__main__":
    main()
