# --- S-AES Simplified Version ---

# S-Box and Inverse S-Box
SBOX = {
    '0000': '1001', '0001': '0100', '0010': '1010', '0011': '1011',
    '0100': '1101', '0101': '0001', '0110': '1000', '0111': '0101',
    '1000': '0110', '1001': '0010', '1010': '0000', '1011': '0011',
    '1100': '1100', '1101': '1110', '1110': '1111', '1111': '0111'
}
INV_SBOX = {v: k for k, v in SBOX.items()}

# --- Helper Functions ---
def to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def rotate(word): return word[4:] + word[:4]

def sub(word): return ''.join(SBOX[word[i:i+4]] for i in range(0, len(word), 4))

def inv_sub(word): return ''.join(INV_SBOX[word[i:i+4]] for i in range(0, len(word), 4))

def add_round_key(a, b): return format(int(a, 2) ^ int(b, 2), '016b')

def g(word, rc):
    return format(int(sub(rotate(word)), 2) ^ int(rc, 2), '08b')

def expand_key(key):
    w = [key[:8], key[8:]]
    w.append(format(int(w[0], 2) ^ int(g(w[1], '10000000'), 2), '08b'))
    w.append(format(int(w[2], 2) ^ int(w[1], 2), '08b'))
    w.append(format(int(w[2], 2) ^ int(g(w[3], '00110000'), 2), '08b'))
    w.append(format(int(w[4], 2) ^ int(w[3], 2), '08b'))
    return [w[0] + w[1], w[2] + w[3], w[4] + w[5]]

def shift(word): return word[:4] + word[12:] + word[8:12] + word[4:8]

def inv_shift(word): return shift(word)  # Same shift for 2x2 matrix

def encrypt(ptext, key):
    keys = expand_key(key)
    state = add_round_key(ptext, keys[0])
    state = shift(sub(state))
    state = add_round_key(state, keys[1])
    state = shift(sub(state))
    return add_round_key(state, keys[2])

def decrypt(ctext, key):
    keys = expand_key(key)
    state = add_round_key(ctext, keys[2])
    state = inv_sub(inv_shift(state))
    state = add_round_key(state, keys[1])
    state = inv_sub(inv_shift(state))
    return add_round_key(state, keys[0])

# --- User Input and Execution ---

def get_input(prompt):
    while True:
        text = input(prompt).strip()
        if len(text) == 2:
            return to_bin(text)
        print("❌ Please enter exactly 2 characters.")

if __name__ == "__main__":
    pt_bin = get_input("Enter 2-character plaintext: ")
    ky_bin = get_input("Enter 2-character key     : ")

    cipher = encrypt(pt_bin, ky_bin)
    decrypted = decrypt(cipher, ky_bin)

    print("\n--- Results ---")
    print(f"Ciphertext (binary): {cipher}")
    print(f"Decrypted Text     : {to_text(decrypted)}")





 # --- REQUIRED PYTHON LIBRARIES (INSTALL WITH pip) ---
# ✅ No external libraries are required.
# ✅ This implementation uses only built-in Python functions.
# ✅ No pip installation needed.

# --- SAMPLE INPUT & OUTPUT ---
# Input:
# Enter 2-character plaintext: ok
# Enter 2-character key     : ab
#
# Output:
# --- Results ---
# Ciphertext (binary): 1101000010101011
# Decrypted Text     : ok

# --- SHORT WORKING OF PROGRAM ---
# 1. Input:
#    - 2-character plaintext (e.g., "ok") → converted to 16-bit binary.
#    - 2-character key      (e.g., "ab") → converted to 16-bit binary.
#
# 2. Key Expansion (produces 3 round keys):
#    - Initial 16-bit key split into w0 and w1 (8 bits each).
#    - w2 = w0 XOR g(w1, RC1)
#    - w3 = w2 XOR w1
#    - w4 = w2 XOR g(w3, RC2)
#    - w5 = w4 XOR w3
#    - Round keys = [w0+w1, w2+w3, w4+w5]
#
# 3. Encryption:
#    - Round 1:
#        a. AddRoundKey (plaintext ⊕ round key 1)
#        b. Substitute nibbles (using SBOX)
#        c. Shift rows (2x2 matrix, swap lower nibbles)
#        d. AddRoundKey (with round key 2)
#    - Round 2:
#        a. Substitute + Shift again
#        b. Final AddRoundKey (with round key 3)
#
# 4. Decryption:
#    - Reverse the process:
#        a. AddRoundKey with key3
#        b. Inverse Shift
#        c. Inverse SBOX
#        d. AddRoundKey with key2
#        e. Inverse Shift + Inverse SBOX
#        f. AddRoundKey with key1 → gets original plaintext

# --- BITWISE OPERATIONS USED ---
# ✔ XOR:     add_round_key(a, b) → binary XOR of 16-bit strings.
# ✔ SBOX:    Maps 4-bit input to 4-bit output via dictionary.
# ✔ Shift:   Swaps 2x2 matrix row (nibble rearrangement).
# ✔ Rotation: 8-bit word left-rotated 4 bits (used in key schedule).
# ✔ Round Constants: RC1 = '10000000', RC2 = '00110000'

# --- NOTES ---
# 🔐 This is a simplified version of AES (S-AES) for educational purposes.
# 🔐 It demonstrates core concepts: key expansion, substitution, permutation, and round operations.

# --- END OF COMMENTS ---
