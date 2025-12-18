# file-encryption
Disclaimer: This is a hobby project and has not been audited for issues.

Files are encrypted using AES with a 256-bit key in CBC mode. Files are authenticated with HMAC-SHA256 Encrypt-then-MAC. Keys are derived using Argon2id with parameters memory=2GiB, iterations=2, lanes=4.

<img width="716" height="619" alt="Screenshot 2025-12-17 222006" src="https://github.com/user-attachments/assets/4994675c-e9ff-423e-af43-5e47f6f86ec0" />
