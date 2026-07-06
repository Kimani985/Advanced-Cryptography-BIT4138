print("=" * 55)
print("      SECURE KEY EXCHANGE SIMULATOR")
print("=" * 55)

# Public values
p = 23
g = 5

print(f"\nPublic Prime (p): {p}")
print(f"Generator (g): {g}")

# User input
alice_private = int(input("\nEnter Alice's private key: "))
bob_private = int(input("Enter Bob's private key: "))

# Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Generate shared secret
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)

print("\n========== RESULTS ==========")
print(f"Alice Public Key : {alice_public}")
print(f"Bob Public Key   : {bob_public}")
print(f"Alice Secret Key : {alice_secret}")
print(f"Bob Secret Key   : {bob_secret}")

if alice_secret == bob_secret:
    print("\nSecure key exchange successful.")
    print("Shared Secret:", alice_secret)
else:
    print("\nKey exchange failed.")
    python secure_key_exchange.py