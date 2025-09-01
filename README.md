# Digital Signature & Transaction Verification Demo

This Python script demonstrates the fundamental cryptographic process that secures blockchain transactions: digital signatures.

## Core Concepts Demonstrated

1.  **Key Generation:** A unique pair of keys (private and public) is created.
    -   The **Private Key** must be kept secret. It is used to create signatures (i.e., authorize transactions).
    -   The **Public Key** can be shared with anyone. It is used to verify signatures.

2.  **Signing:** A transaction message is cryptographically "signed" using the private key. This produces a unique digital signature that acts as a seal of approval from the key owner.

3.  **Verification:** The public key, the original message, and the signature are used to check if the signature is authentic.
    -   If the verification is successful, it proves that the transaction was authorized by the owner of the private key.
    -   If the message is altered in any way (even by a single character), the verification will fail.

## How the Script Works
The script performs a full workflow:
1.  It generates a new private/public key pair.
2.  It defines a sample transaction message and signs it with the private key.
3.  It then runs two verification checks:
    -   One with the **original, unaltered message**, which passes.
    -   One with a **tampered message**, which fails.

This clearly shows how digital signatures prevent unauthorized changes to transactions on the blockchain.

## How to Run

### 1. Installation
This script requires the `cryptography` library. Install it using pip:
```bash

pip install cryptography

## OUTPUT
<img width="929" height="437" alt="Screenshot 2025-09-01 191514" src="https://github.com/user-attachments/assets/a237b2a1-3858-4e00-9cf4-7a306235a7ef" />

