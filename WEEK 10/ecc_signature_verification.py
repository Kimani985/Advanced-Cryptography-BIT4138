from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

print("=" * 60)
print("        ECC DIGITAL SIGNATURE VERIFICATION")
print("=" * 60)

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Message
message = input("\nEnter a message: ").encode()

# Sign the message
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

print("\nSignature Generated Successfully!")

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("\nSignature Verification: SUCCESS")
    print("The message is authentic and has not been modified.")
except InvalidSignature:
    print("\nSignature Verification: FAILED")
    print("The message integrity could not be verified.")