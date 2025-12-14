# file-encryption
Disclaimer: This is a hobby project and has not been audited for issues.

Files are encrypted using AES with a 256-bit key in CBC mode. Files are authenticated with HMAC-SHA256 Encrypt-then-MAC. Keys are derived using Argon2id with parameters memory=2GiB, iterations=2, lanes=4.
