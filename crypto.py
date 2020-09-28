import random
from math import gcd

# Andromeda Kepecs 
# Redmond Block C
# September 22, 2020

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


# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    print(decrypt_vigenere("O", "ONEINPUT"))
    private_key = generate_private_key()
    public_key = create_public_key(private_key)

if __name__ == "__main__":
    main()
