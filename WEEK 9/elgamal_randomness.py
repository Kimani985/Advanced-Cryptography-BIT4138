import random

print("=" * 60)
print("      ELGAMAL RANDOMNESS DEMONSTRATION")
print("=" * 60)

# Public parameters
p = 467
g = 2

# Receiver's keys
private_key = random.randint(2, p - 2)
public_key = pow(g, private_key, p)

message = int(input("\nEnter message (less than 467): "))

print("\nEncrypting the SAME message five times...\n")

for i in range(1, 6):
    k = random.randint(2, p - 2)

    c1 = pow(g, k, p)
    shared_secret = pow(public_key, k, p)
    c2 = (message * shared_secret) % p

    print(f"Attempt {i}")
    print(f"C1 = {c1}")
    print(f"C2 = {c2}")
    print("-" * 35)