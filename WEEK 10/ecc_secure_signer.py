from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

print("=" * 65)
print("              ECC SECURE SIGNER")
print("=" * 65)

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

message = input("\nEnter the message to sign: ").encode()

# Generate Signature
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

print("\nMessage Successfully Signed!")

print("\nSignature (Hex):")
print(signature.hex())

print("\nVerifying Signature...")

try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )

    print("\nSTATUS : VERIFIED")
    print("The message is authentic.")
    print("No tampering detected.")

except InvalidSignature:

    print("\nSTATUS : INVALID")
    print("The message integrity has been compromised.")

print("\nOperation Completed Successfully.")