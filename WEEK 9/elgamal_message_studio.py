import random

print("=" * 60)
print("           ELGAMAL MESSAGE STUDIO")
print("=" * 60)

# Public Parameters
p = 467
g = 2

# Generate Keys
private_key = random.randint(2, p - 2)
public_key = pow(g, private_key, p)

print("\nGenerated Keys")
print("-" * 30)
print(f"Prime (p): {p}")
print(f"Generator (g): {g}")
print(f"Private Key: {private_key}")
print(f"Public Key : {public_key}")

message = int(input("\nEnter message (less than 467): "))

# Encryption
k = random.randint(2, p - 2)

c1 = pow(g, k, p)
shared_secret = pow(public_key, k, p)
c2 = (message * shared_secret) % p

print("\n===== ENCRYPTION =====")
print(f"Ciphertext (C1): {c1}")
print(f"Ciphertext (C2): {c2}")

# Decryption
shared_secret_receiver = pow(c1, private_key, p)
inverse = pow(shared_secret_receiver, -1, p)
decrypted = (c2 * inverse) % p

print("\n===== DECRYPTION =====")
print(f"Recovered Message: {decrypted}")

if decrypted == message:
    print("\nMessage Verified Successfully!")
else:
    print("\nVerification Failed!")