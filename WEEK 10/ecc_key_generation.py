from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

print("=" * 60)
print("        ELLIPTIC CURVE KEY GENERATION")
print("=" * 60)

# Generate ECC private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Generate public key
public_key = private_key.public_key()

print("\nECC Key Pair Generated Successfully!")

# Serialize the keys
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("\nPrivate Key:\n")
print(private_bytes.decode())

print("\nPublic Key:\n")
print(public_bytes.decode())