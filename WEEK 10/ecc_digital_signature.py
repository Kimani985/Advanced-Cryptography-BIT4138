from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

print("=" * 60)
print("      ECC DIGITAL SIGNATURE GENERATION")
print("=" * 60)

# Generate ECC private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Message
message = input("\nEnter a message to sign: ").encode()

# Generate signature
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

print("\nMessage:")
print(message.decode())

print("\nDigital Signature (Hex):")
print(signature.hex())

print("\nSignature generated successfully!")