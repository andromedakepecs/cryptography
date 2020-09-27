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
    for i in range(len(plaintext)):
        textCode = ord(plaintext[i])
        offset = ord(keyword[i]) - 65
        newCode = textCode + offset
        if newCode > 90:
            newCode -= 26
        newString += chr(newCode)
    return newString

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    newString = ''
    for i in range(len(ciphertext)):
        textCode = ord(ciphertext[i])
        offset = ord(keyword[i]) - 65
        newCode = textCode - offset
        if newCode < 65:
            newCode += 26
        newString += chr(newCode)
    return newString

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    

if __name__ == "__main__":
    main()
