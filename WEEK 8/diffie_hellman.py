print("=" * 50)
print("DIFFIE-HELLMAN KEY EXCHANGE")
print("=" * 50)

# Public values
p = 23
g = 5

print(f"\nPublic Prime (p): {p}")
print(f"Generator (g): {g}")

# Private keys
alice_private = 6
bob_private = 15

print(f"\nAlice Private Key: {alice_private}")
print(f"Bob Private Key: {bob_private}")

# Public keys
alice_public = (g ** alice_private) % p
bob_public = (g ** bob_private) % p

print(f"\nAlice Public Key: {alice_public}")
print(f"Bob Public Key: {bob_public}")

# Shared secret
alice_secret = (bob_public ** alice_private) % p
bob_secret = (alice_public ** bob_private) % p

print(f"\nAlice Shared Secret: {alice_secret}")
print(f"Bob Shared Secret: {bob_secret}")

if alice_secret == bob_secret:
    print("\nKey Exchange Successful!")
else:
    print("\nKey Exchange Failed!")