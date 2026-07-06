from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

print("=" * 65)
print("        DIGITAL SIGNATURE TAMPERING DETECTOR")
print("=" * 65)

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Original message
original_message = input("\nEnter the original message: ").encode()

# Sign the original message
signature = private_key.sign(
    original_message,
    ec.ECDSA(hashes.SHA256())
)

print("\nOriginal message signed successfully.")

# Simulate tampering
tampered_message = (original_message.decode() + " (Modified)").encode()

print("\nOriginal Message:")
print(original_message.decode())

print("\nTampered Message:")
print(tampered_message.decode())

print("\nChecking signature against the tampered message...")

try:
    public_key.verify(
        signature,
        tampered_message,
        ec.ECDSA(hashes.SHA256())
    )

    print("\nVerification Result: SUCCESS")
    print("No tampering detected.")

except InvalidSignature:

    print("\nVerification Result: FAILED")
    print("Tampering Detected!")
    print("The digital signature is no longer valid because the message was altered.")

print("\nIntegrity Check Completed.")