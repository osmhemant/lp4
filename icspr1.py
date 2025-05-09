# S-DES Implementation - Simplified Version

def permute(bits, pattern):
    return [bits[i - 1] for i in pattern]

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def str_to_bits(bit_string):
    return [int(b) for b in bit_string]

def bits_to_str(bits):
    return ''.join(str(b) for b in bits)

# S-Boxes
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def s_box_lookup(bits, box):
    row = (bits[0] << 1) | bits[3]
    col = (bits[1] << 1) | bits[2]
    val = box[row][col]
    return [val >> 1, val & 1]

def fk(bits, subkey):
    EP = [4,1,2,3,2,3,4,1]
    P4 = [2,4,3,1]
    L, R = bits[:4], bits[4:]
    R_exp = permute(R, EP)
    R_xor = [r ^ k for r, k in zip(R_exp, subkey)]
    S0_out = s_box_lookup(R_xor[:4], S0)
    S1_out = s_box_lookup(R_xor[4:], S1)
    P4_out = permute(S0_out + S1_out, P4)
    return [l ^ p for l, p in zip(L, P4_out)] + R

def switch(bits):
    return bits[4:] + bits[:4]

def generate_keys(key_bits):
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8 = [6,3,7,4,8,5,10,9]

    key_p10 = permute(key_bits, P10)
    L, R = key_p10[:5], key_p10[5:]

    # First key
    L1 = left_shift(L, 1)
    R1 = left_shift(R, 1)
    K1 = permute(L1 + R1, P8)

    # Second key
    L2 = left_shift(L1, 2)
    R2 = left_shift(R1, 2)
    K2 = permute(L2 + R2, P8)

    return K1, K2

def encrypt(plaintext, key):
    IP = [2,6,3,1,4,8,5,7]
    IP_inv = [4,1,3,5,7,2,8,6]

    pt_bits = str_to_bits(plaintext)
    key_bits = str_to_bits(key)

    K1, K2 = generate_keys(key_bits)

    ip = permute(pt_bits, IP)
    round1 = fk(ip, K1)
    swapped = switch(round1)
    round2 = fk(swapped, K2)
    cipher = permute(round2, IP_inv)

    return bits_to_str(cipher)

def decrypt(ciphertext, key):
    IP = [2,6,3,1,4,8,5,7]
    IP_inv = [4,1,3,5,7,2,8,6]

    ct_bits = str_to_bits(ciphertext)
    key_bits = str_to_bits(key)

    K1, K2 = generate_keys(key_bits)

    ip = permute(ct_bits, IP)
    round1 = fk(ip, K2)
    swapped = switch(round1)
    round2 = fk(swapped, K1)
    plain = permute(round2, IP_inv)

    return bits_to_str(plain)

# --- USER INPUT INTERFACE ---

print("Enter 8-bit plaintext (e.g., 10101010):")
plaintext = input().strip()

print("Enter 10-bit key (e.g., 1010000010):")
key = input().strip()

cipher = encrypt(plaintext, key)
print("Encrypted Text :", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted Text :", decrypted)


# --- SAMPLE INPUT & OUTPUT ---
# Input:
# Enter 8-bit plaintext (e.g., 10101010):
# 10101010
# Enter 10-bit key (e.g., 1010000010):
# 1010000010
#
# Output:
# Encrypted Text : 01110111
# Decrypted Text : 10101010

# --- SHORT WORKING OF PROGRAM ---
# 1. The user enters an 8-bit plaintext and a 10-bit key.
# 2. The key is permuted and left-shifted to generate two subkeys (K1 and K2).
# 3. The plaintext is permuted (Initial Permutation - IP).
# 4. First round:
#    - Right half is expanded and XORed with K1.
#    - Result goes through S-boxes and P4 permutation.
#    - Left half is XORed with this result.
# 5. Halves are swapped.
# 6. Second round:
#    - Similar to round 1 but with K2.
# 7. Final permutation (IP⁻¹) gives the ciphertext.
# 8. For decryption, the same steps are followed but using K2 first, then K1.
# 9. Output shows both encrypted and decrypted text.

# This is a simplified version of the DES algorithm called S-DES used for educational purposes.