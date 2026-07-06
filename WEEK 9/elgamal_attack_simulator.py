import random

print("=" * 60)
print("          ELGAMAL ATTACK SIMULATOR")
print("=" * 60)

# Public parameters
p = 467
g = 2

# Receiver's private and public keys
private_key = random.randint(2, p - 2)
public_key = pow(g, private_key, p)

print("\nPublic Parameters")
print("------------------------------")
print(f"Prime (p): {p}")
print(f"Generator (g): {g}")
print(f"Public Key: {public_key}")

# Original message
message = int(input("\nEnter message (less than 467): "))

# Sender encrypts the message
k = random.randint(2, p - 2)

c1 = pow(g, k, p)
shared_secret = pow(public_key, k, p)
c2 = (message * shared_secret) % p

print("\n========== MESSAGE SENT ==========")
print(f"Ciphertext C1: {c1}")
print(f"Ciphertext C2: {c2}")

# Attacker intercepts
print("\n========== ATTACK SIMULATION ==========")
print("Attacker intercepted:")
print(f"Public Key : {public_key}")
print(f"Ciphertext : ({c1}, {c2})")
print("Private Key: NOT AVAILABLE")

print("\nAttempting to recover plaintext...")

print("Result: FAILED")
print("Reason: Private key is required to compute the shared secret.")

# Legitimate receiver decrypts
shared_secret_receiver = pow(c1, private_key, p)
inverse = pow(shared_secret_receiver, -1, p)
decrypted_message = (c2 * inverse) % p

print("\n========== LEGITIMATE RECEIVER ==========")
print(f"Recovered Message: {decrypted_message}")

if decrypted_message == message:
    print("\nSecure communication successful!")
else:
    print("\nDecryption failed!")
    