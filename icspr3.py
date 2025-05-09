import random

# Step 1: Publicly shared prime number (p) and primitive root (g)
p = 23   # Prime number
g = 5     # Primitive root modulo p
print(f"Publicly shared values:\nPrime number (p): {p}\nPrimitive root (g): {g}\n")

# Step 2: Each person chooses a private key
a = random.randint(1, p-2)  # Alice's private key
b = random.randint(1, p-2)  # Bob's private key
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}\n")

# Step 3: Calculate the public keys
A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key
print(f"Alice's public key (A): {A}")
print(f"Bob's public key (B): {B}\n")

# Step 4: Exchange public keys and calculate the shared secret
shared_secret_alice = pow(B, a, p)  # Alice computes shared key
shared_secret_bob = pow(A, b, p)    # Bob computes shared key

print(f"Alice's computed shared secret: {shared_secret_alice}")
print(f"Bob's computed shared secret: {shared_secret_bob}\n")

# Step 5: Verify that both shared secrets are the same
if shared_secret_alice == shared_secret_bob:
    print(f"✅ Success! Shared secret key established: {shared_secret_alice}")
else:
    print("❌ Error! Shared secrets do not match.")

# --- REQUIRED PYTHON LIBRARIES (INSTALL WITH pip) ---
# ✅ No external libraries are required.
# ✅ This implementation uses only built-in Python functions.
# ✅ The random module is used to generate random private keys.

# --- SAMPLE INPUT & OUTPUT ---
# Sample Output when run:
# Publicly shared values:
# Prime number (p): 23
# Primitive root (g): 5
# Alice's private key (a): 4
# Bob's private key (b): 3
# Alice's public key (A): 4
# Bob's public key (B): 10
# Alice's computed shared secret: 13
# Bob's computed shared secret: 13
# ✅ Success! Shared secret key established: 13

# --- SHORT WORKING OF PROGRAM ---
# 1. Public values:
#    - A prime number (p) and a primitive root modulo p (g) are agreed upon by Alice and Bob.
#    - These are public and known to both parties.
#
# 2. Private keys:
#    - Alice and Bob each select their private keys (a and b).
#    - These are secret and kept private.
#
# 3. Public keys:
#    - Alice computes her public key (A) as A = g^a mod p and sends it to Bob.
#    - Bob computes his public key (B) as B = g^b mod p and sends it to Alice.
#
# 4. Shared secret:
#    - Alice computes the shared secret using Bob's public key: shared_secret_alice = B^a mod p.
#    - Bob computes the shared secret using Alice's public key: shared_secret_bob = A^b mod p.
#    - Both Alice and Bob arrive at the same shared secret, ensuring secure communication.
#
# 5. Verification:
#    - Both Alice and Bob verify that their computed shared secrets match.
#    - If they match, the key exchange is successful, and they can use the shared secret for encryption.
#    - If not, there is an error in the process (although it should not happen).

# --- BITWISE CALCULATIONS USED ---
# ✔ Modular exponentiation: 
#    - Alice and Bob compute their public keys using: 
#      A = g^a mod p, B = g^b mod p.
#    - The shared secret is calculated using: shared_secret = (other party's public key) ^ private key mod p.
# ✔ Random private key: Each party selects a random private key between 1 and p-2.
#
# Example:
#    - p = 23, g = 5
#    - Alice's private key a = 4 → Alice's public key A = 5^4 mod 23 = 625 mod 23 = 4
#    - Bob's private key b = 3 → Bob's public key B = 5^3 mod 23 = 125 mod 23 = 10
#
# Shared secret:
#    - Alice calculates shared_secret = 10^4 mod 23 = 10000 mod 23 = 13
#    - Bob calculates shared_secret = 4^3 mod 23 = 64 mod 23 = 13
#    - Both Alice and Bob obtain the same shared secret: 13

# --- NOTES ---
# 🔐 This implementation demonstrates the **Diffie-Hellman key exchange** algorithm.
# 🔐 It allows two parties to securely establish a shared secret over an insecure channel.
# 🔐 The strength of the Diffie-Hellman protocol relies on the difficulty of computing discrete logarithms in modular arithmetic.

# --- END OF COMMENTS ---
