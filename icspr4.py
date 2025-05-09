import random
from sympy import randprime, gcd
from Crypto.Util.number import inverse

# Generate RSA key pairs
def generate_keys(bit_length=16):
    p = randprime(2**(bit_length - 1), 2**bit_length)
    q = randprime(2**(bit_length - 1), 2**bit_length)
    while p == q:
        q = randprime(2**(bit_length - 1), 2**bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = inverse(e, phi)

    return (e, n), (d, n)

# Encrypt each character
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt each character
def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(c, d, n)) for c in ciphertext])

# Main flow
def main():
    public_key, private_key = generate_keys()

    print("🔐 Public Key:", public_key)
    print("🔒 Private Key:", private_key)

    message = "Hello RSA!"
    print("\n📨 Original Message:", message)

    cipher = encrypt(message, public_key)
    print("🔒 Ciphertext:", cipher)

    decrypted = decrypt(cipher, private_key)
    print("🔓 Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()



    # --- REQUIRED PYTHON LIBRARIES (INSTALL WITH pip) ---
# ✅ Install necessary libraries via pip:
#    - sympy (for random prime generation)
#    - pycryptodome (for inverse function)
# pip install sympy pycryptodome

# --- SAMPLE INPUT & OUTPUT ---
# Sample Output (actual values may vary):
# 🔐 Public Key: (e, n) → e = encryption exponent, n = modulus
# 🔒 Private Key: (d, n) → d = decryption exponent, n = modulus
#
# 📨 Original Message: Hello RSA!
# 🔒 Ciphertext: [list of encrypted integers, one for each character]
# 🔓 Decrypted Message: Hello RSA!

# Example:
# 🔐 Public Key: (60991, 51341)
# 🔒 Private Key: (13391, 51341)
# 📨 Original Message: Hello RSA!
# 🔒 Ciphertext: [15169, 48249, 36786, 36786, 14434, 18040, 44017, 16462, 2340, 50802]
# 🔓 Decrypted Message: Hello RSA!

# --- SHORT WORKING OF PROGRAM ---
# 1. Generate two large random primes p and q.
#    - These primes are chosen randomly from a specified bit length range.
# 2. Compute the modulus n = p * q and Euler's totient function φ(n) = (p - 1) * (q - 1).
# 3. Choose the encryption exponent e:
#    - e is chosen such that 1 < e < φ(n), and gcd(e, φ(n)) = 1 (ensures e and φ(n) are coprime).
# 4. Compute the private key exponent d:
#    - d is calculated as the modular inverse of e with respect to φ(n), i.e., (d * e) ≡ 1 mod φ(n).
# 5. Encryption:
#    - For each character in the message, its ASCII value is raised to the power of e and reduced modulo n.
#    - This produces the ciphertext (encrypted data).
# 6. Decryption:
#    - For each ciphertext integer, we compute (cipher_char^d) mod n to get the original character back.
#
# Keys:
#    - Public Key = (e, n)
#    - Private Key = (d, n)
#
# This RSA implementation uses small prime numbers (16-bit) for simplicity. 
# In real-world scenarios, larger primes (typically 2048-bits or more) are used for security.

# --- BITWISE / MODULAR MATH CALCULATIONS ---
# - `pow(base, exp, mod)` is used to efficiently calculate (base^exp) % mod in Python.
# - The modular inverse is computed using `Crypto.Util.number.inverse(e, φ(n))` to find d.
# - RSA encryption and decryption are based on **modular exponentiation**.
# - RSA security relies on the **difficulty of factoring** the large modulus n = p * q.
#
# Example:
#    - p = 17, q = 19
#    - n = 17 * 19 = 323
#    - φ(n) = (17 - 1) * (19 - 1) = 288
#    - e = 5 (random choice such that gcd(5, 288) = 1)
#    - d = inverse(5, 288) = 173
#
# In encryption, for a message "Hello RSA!", each character is converted to an integer and encrypted as:
#    cipher_char_
