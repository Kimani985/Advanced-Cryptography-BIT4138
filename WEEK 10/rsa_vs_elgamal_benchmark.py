import random
import time
from Crypto.PublicKey import RSA

print("=" * 65)
print("        RSA VS ELGAMAL PERFORMANCE BENCHMARK")
print("=" * 65)

# ---------------- RSA ---------------- #

message = 123

# RSA Key Generation
start = time.perf_counter()
rsa_key = RSA.generate(2048)
rsa_keygen = time.perf_counter() - start

# RSA Encryption (simulation)
e = rsa_key.e
n = rsa_key.n

start = time.perf_counter()
rsa_cipher = pow(message, e, n)
rsa_encrypt = time.perf_counter() - start

# RSA Decryption
d = rsa_key.d

start = time.perf_counter()
rsa_plain = pow(rsa_cipher, d, n)
rsa_decrypt = time.perf_counter() - start


# ---------------- ElGamal ---------------- #

p = 467
g = 2

# ElGamal Key Generation
start = time.perf_counter()

private_key = random.randint(2, p - 2)
public_key = pow(g, private_key, p)

elgamal_keygen = time.perf_counter() - start

# ElGamal Encryption
k = random.randint(2, p - 2)

start = time.perf_counter()

c1 = pow(g, k, p)
shared_secret = pow(public_key, k, p)
c2 = (message * shared_secret) % p

elgamal_encrypt = time.perf_counter() - start

# ElGamal Decryption

start = time.perf_counter()

shared_receiver = pow(c1, private_key, p)
inverse = pow(shared_receiver, -1, p)
plain = (c2 * inverse) % p

elgamal_decrypt = time.perf_counter() - start


print("\nPerformance Comparison")
print("-" * 65)

print("{:<12} {:<12} {:<12} {:<12}".format(
    "Algorithm",
    "Key Gen",
    "Encrypt",
    "Decrypt"
))

print("-" * 65)

print("{:<12} {:<12.6f} {:<12.6f} {:<12.6f}".format(
    "RSA",
    rsa_keygen,
    rsa_encrypt,
    rsa_decrypt
))

print("{:<12} {:<12.6f} {:<12.6f} {:<12.6f}".format(
    "ElGamal",
    elgamal_keygen,
    elgamal_encrypt,
    elgamal_decrypt
))

print("\nRecovered RSA Message :", rsa_plain)
print("Recovered ElGamal Message :", plain)