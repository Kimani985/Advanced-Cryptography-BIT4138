import random

print("=" * 55)
print("           ELGAMAL ENCRYPTION & DECRYPTION")
print("=" * 55)

# Public parameters
p = 467
g = 2

# Receiver's private key
private_key = random.randint(2, p - 2)

# Receiver's public key
public_key = pow(g, private_key, p)

message = int(input("\nEnter message (less than 467): "))

# Sender chooses random number
k = random.randint(2, p - 2)

# Encryption
c1 = pow(g, k, p)
shared_secret = pow(public_key, k, p)
c2 = (message * shared_secret) % p

print("\n===== ENCRYPTION =====")
print("Ciphertext (C1):", c1)
print("Ciphertext (C2):", c2)

# Decryption
shared_secret_receiver = pow(c1, private_key, p)
inverse = pow(shared_secret_receiver, -1, p)
decrypted_message = (c2 * inverse) % p

print("\n===== DECRYPTION =====")
print("Recovered Message:", decrypted_message)

if decrypted_message == message:
    print("\nDecryption Successful!")
else:
    print("\nDecryption Failed!")