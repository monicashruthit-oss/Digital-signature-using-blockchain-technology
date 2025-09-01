# Before running, you must install the required library:
# pip install cryptography

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

def generate_keys():
    """Generates an elliptic curve private and public key pair."""
    # SECP256K1 is the curve used by Bitcoin and Ethereum
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    """Signs a message with the given private key."""
    # Messages must be in bytes, so we encode the string
    message_bytes = message.encode('utf-8')
    
    signature = private_key.sign(
        message_bytes,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, message, signature):
    """Verifies a signature using the public key and original message."""
    message_bytes = message.encode('utf-8')
    
    try:
        public_key.verify(
            signature,
            message_bytes,
            ec.ECDSA(hashes.SHA256())
        )
        # If the above line does not raise an exception, the signature is valid.
        return True
    except InvalidSignature:
        # The signature is invalid if an exception is raised.
        return False

if __name__ == "__main__":
    # --- 1. Key Generation ---
    print("--- 1. Generating Keys ---")
    my_private_key, my_public_key = generate_keys()
    print("Keys generated successfully.")
    # In a real app, you would save the private key securely!
    # The public key can be shared freely.

    # --- 2. Create and Sign a Transaction ---
    print("\n--- 2. Creating and Signing a Transaction ---")
    original_transaction = "Send 1.5 BTC from Alice to Bob"
    signature = sign_message(my_private_key, original_transaction)
    print(f"Original Transaction: '{original_transaction}'")
    print(f"Signature (in hex):   {signature.hex()}")

    # --- 3. Verification ---
    print("\n--- 3. Verifying the Signature ---")
    
    # Scenario A: Verifying the legitimate transaction
    is_valid = verify_signature(my_public_key, original_transaction, signature)
    print(f"Is the original signature valid? -> {is_valid}")

    # Scenario B: An attacker tampers with the transaction
    tampered_transaction = "Send 100 BTC from Alice to Bob"
    is_tampered_valid = verify_signature(my_public_key, tampered_transaction, signature)
    print(f"Is the signature valid for a TAMPERED transaction? -> {is_tampered_valid}")
    
    print("\nThis demonstrates that a signature is only valid for the exact message it was created for.")