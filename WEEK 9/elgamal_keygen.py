import random

print("=" * 55)
print("        ELGAMAL KEY GENERATION")
print("=" * 55)

# Public parameters
p = 467          # Prime number
g = 2            # Generator

# Private key
private_key = random.randint(2, p - 2)

# Public key
public_key = pow(g, private_key, p)

print("\nPublic Parameters")
print("-----------------")
print(f"Prime (p): {p}")
print(f"Generator (g): {g}")

print("\nGenerated Keys")
print("-----------------")
print(f"Private Key: {private_key}")
print(f"Public Key : {public_key}")

print("\nKey generation completed successfully.")
