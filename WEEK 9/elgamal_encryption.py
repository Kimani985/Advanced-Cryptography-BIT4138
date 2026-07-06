import random

print("=" * 55)
print("           ELGAMAL ENCRYPTION")
print("=" * 55)

# Public parameters
p = 467
g = 2

# Receiver's private key
private_key = random.randint(2, p - 2)

# Receiver's public key
public_key = pow(g, private_key, p)

message = int(input("\nEnter a message (less than 467): "))

# Sender chooses random value
k = random.randint(2, p - 2)

# Encryption
c1 = pow(g, k, p)
shared_secret = pow(public_key, k, p)
c2 = (message * shared_secret) % p

print("\nReceiver Public Key:", public_key)

print("\nCiphertext")
print("-----------")
print("C1 =", c1)
print("C2 =", c2)