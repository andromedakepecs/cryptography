import random
from math import gcd

# Andromeda Kepecs 
# Redmond Block C

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    newString = ''
    for letter in plaintext:
        textCode = ord(letter)
        if textCode + offset > 90:
            newCode = textCode + offset - 26
        else:
            newCode = textCode + offset
        newString += chr(newCode)
    return newString

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    newString = ''
    for letter in ciphertext:
        textCode = ord(letter)
        if textCode - offset < 65:
            newCode = textCode - offset + 26
        else:
            newCode = textCode - offset
        newString += chr(newCode)
    return newString

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    newString = ''
    keyword_index = 0

    for letter in plaintext:
        textCode = ord(letter)
        offset = ord(keyword[keyword_index]) - 65
        newCode = textCode + offset
        if newCode > 90:
            newCode -= 26
        newString += chr(newCode)

        if (keyword_index + 1) == len(keyword):
            keyword_index = 0
        else: 
            keyword_index += 1

    return newString

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    newString = ''
    keyword_index = 0

    for letter in ciphertext:
        textCode = ord(letter)
        offset = ord(keyword[keyword_index]) - 65
        newCode = textCode - offset
        if newCode < 65:
            newCode += 26
        newString += chr(newCode)

        if (keyword_index + 1) == len(keyword):
            keyword_index = 0
        else: 
            keyword_index += 1

    return newString

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W = []
    total = 5 #arbitrary number greater than 2 so randint works
    for i in range(0, n):
        W.append(random.randint(total + 1, total * 2))
        total += W[i]

    Q = random.randint(total + 1, total * 2)
    R = gen_coprime(Q)

    return W, Q, R

# Arguments: integer
# Returns: coprime integer R
def gen_coprime(Q):
    R = 2
    while gcd(R, Q) != 1:
        R = random.randint(2, Q - 1)
    return R

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    W, Q, R = private_key
    B = []
    
    for i in W:
        B.append((R * i) % Q)

    return tuple(B)

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    cipher_list = []
    for letter in plaintext:
        binary_char = "{0:08b}".format(ord(letter))
        
        C = 0
        for i in range(len(binary_char)):
            C += int(binary_char[i]) * public_key[i]
        cipher_list.append(C)
    return cipher_list
        

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    plaintext = ''
    W, Q, R = private_key
    S = get_modular_inverse(Q, R)
    for C in ciphertext:
        C_prime = C * S % Q
        binary_list = []
        for elt in reversed(W):
            if elt <= C_prime:
                binary_list.append(1)
                C_prime -= elt
            else:
                binary_list.append(0)
        plaintext += chr(bits_to_byte(list(reversed(binary_list))))
    return plaintext

# Arguments: list of bits (binary)
# Returns: int sum (decimal)
def bits_to_byte(bits):
   return bits[0]*128 + bits[1]*64 + bits[2]*32 + bits[3]*16 + bits[4]*8 + bits[5]*4 + bits[6]*2 + bits[7]

# Arguments: two coprime ints
# Returns: int modular inverse 
def get_modular_inverse(Q, R):
    S = 0
    while (R * S) % Q != 1:
        S += 1
    return S

# Testing code
def main():
    # Caeser
    print('Caesar encryption: ' + encrypt_caesar("ZEBRA", 25))
    print('Caesar decryption: ' + decrypt_caesar("YDAQZ", 25))
    print("")

    # Vigenere 
    print('Vigenere encryption: ' + encrypt_vigenere("IMISSCODINGIN", "JAVA"))
    print('Vigenere decryption: ' + decrypt_vigenere("RMDSBCJDRNBIW", "JAVA"))
    print("")

    # MHKC
    private_key = generate_private_key()
    print('Private key: ' + str(private_key))
    public_key = create_public_key(private_key)
    print('Public key: ' + str(public_key))
    encrypted = encrypt_mhkc("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG", public_key)
    print('Encrypted: ' + str(encrypted))
    print('Decrypted: ' + decrypt_mhkc(encrypted, private_key))

if __name__ == "__main__":
    main()
