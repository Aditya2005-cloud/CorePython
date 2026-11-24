# Password Cracking Lab (Beginner, Python)

A self-contained, legal, local lab for learning how password cracking and
password-strength auditing actually work — using only passwords you generate
yourself. Everything here runs on fake accounts in `hashes/`; nothing touches
anyone else's data or any live system.

## What's inside

```
password-lab/
├── wordlists/
│   └── common.txt          # small list of common weak passwords
├── scripts/
│   ├── generate_hashes.py  # creates a fake "leaked database" to crack
│   ├── crack.py            # your own dictionary + brute-force cracker
│   └── strength_audit.py   # password strength / crack-time estimator
└── hashes/                 # generated hash files land here
```

## 1. Generate the target hashes

```bash
cd scripts
python3 generate_hashes.py
```

This creates `hashes/md5.txt`, `sha1.txt`, `sha256.txt`, and
`shadow_like.txt` (a realistic `sha512crypt` hash like real
`/etc/shadow` uses), each mapping `user:hash` for 6 fake accounts with a
mix of weak and semi-weak passwords. It also prints the answer key so you
can check your cracker's output.

## 2. Crack them with your own Python cracker

```bash
# Dictionary attack on raw MD5 hashes
python3 crack.py --mode dict --algo md5 --hashfile ../hashes/md5.txt

# Dictionary attack on the slow, salted sha512crypt hashes
python3 crack.py --mode dict --algo sha512crypt --hashfile ../hashes/shadow_like.txt

# Brute force (tries every combination up to a given length)
python3 crack.py --mode brute --algo md5 --hashfile ../hashes/md5.txt --maxlen 4
```

Watch the guesses/sec numbers. You should see raw MD5 crack at ~500k
guesses/sec, while the same dictionary against `sha512crypt` runs at under
100 guesses/sec on the same 41-word list — same CPU, same words, 5000x
slower, because `sha512crypt` is *designed* to be slow. That's the entire
reason modern systems use bcrypt/scrypt/argon2/sha512crypt instead of raw
MD5/SHA1 for storing passwords: slow hashing turns a cracking job from
seconds into years.

Passwords that aren't in the wordlist (like `carol`'s `Summer2024!`) won't
crack with `--mode dict` — that's the expected, realistic result. Try
`--mode brute` on the short ones instead (e.g. `frank`'s 4-character
password) to see brute force succeed where dictionary attack can't.

## 3. Do it for real with John the Ripper / Hashcat (on your Kali VM)

Once you've seen how the Python version works, run the same attack with the
real tools — they're just much faster, more optimized versions of exactly
what `crack.py` does.

**John the Ripper:**
```bash
john --format=raw-md5 --wordlist=../wordlists/common.txt ../hashes/md5.txt
john --show --format=raw-md5 ../hashes/md5.txt

# sha512crypt (format is auto-detected from the $6$ prefix)
john --wordlist=../wordlists/common.txt ../hashes/shadow_like.txt
john --show ../hashes/shadow_like.txt

# Brute force / incremental mode
john --format=raw-md5 --incremental=digits ../hashes/md5.txt
```

**Hashcat** (hash file needs just the hash, not `user:hash` — strip the
username column first, e.g. `cut -d: -f2 ../hashes/md5.txt > md5_only.txt`):
```bash
hashcat -m 0    -a 0 md5_only.txt ../wordlists/common.txt   # -m 0 = raw MD5
hashcat -m 100  -a 0 sha1_only.txt ../wordlists/common.txt   # -m 100 = raw SHA1
hashcat -m 1800 -a 0 shadow_only.txt ../wordlists/common.txt # -m 1800 = sha512crypt
hashcat --show -m 0 md5_only.txt
```

Compare John/Hashcat's reported guesses/sec against your Python script's —
that gap is the difference between an interpreted loop and
GPU-parallelized, assembly-optimized hashing.

## 4. Audit password strength

```bash
python3 strength_audit.py "p@ssw0rd"
python3 strength_audit.py --file ../wordlists/common.txt   # audit a whole list
python3 strength_audit.py                                  # hidden prompt
```

For each password it reports:
- whether it's an exact match in the common-password list (instant fail)
- entropy in bits, based on length and character variety actually used
- estimated crack time at three realistic attack speeds (rate-limited
  online login, fast offline hash like raw MD5 on a GPU, and slow offline
  hash like bcrypt/sha512crypt)
- pattern red flags: keyboard walks (`qwerty`, `asdf`), repeated
  characters, trailing years, all-digits, all-lowercase

Try `p@ssw0rd` — the entropy math scores it "MODERATE" because it has 4
character classes, but it's a textbook leetspeak substitution of a
dictionary word. A real attacker's wordlist + mangling rules (John's
`--rules`, Hashcat's `-r rules/best64.rule`) would still crack it almost
instantly. This is the key lesson: entropy estimates assume random
guessing, but humans are predictable, so rule-based + dictionary attacks
beat pure brute force against human-chosen passwords almost every time.

## Suggested next steps

- Add rule-mangling to `crack.py` yourself (e.g. try `word + "123"`,
  `word` with `a→@`, `o→0`, `e→3` substitutions) and see how many more
  passwords it catches.
- Point John at the same hashes with `--rules` on and compare.
- Swap in a real `/etc/shadow` line from a VM you own (never someone
  else's) to see it work against a genuine system hash.
- Feed `strength_audit.py` a leaked-password list (e.g. rockyou.txt,
  already on Kali at `/usr/share/wordlists/rockyou.txt.gz`) instead of the
  tiny `common.txt` for a much stronger "is this common" check.

## Scope note

Only crack hashes you generated yourself or have explicit written
permission to test. Cracking someone else's credentials without
authorization is illegal in most jurisdictions regardless of intent.
