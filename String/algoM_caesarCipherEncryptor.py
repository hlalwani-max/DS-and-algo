# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
def encryption(alpha, key):
    ascii = ord(alpha) + key % 26

    if ascii <= 122:
        return chr(ascii)
    else:
        return chr(96 + ascii % 122)


def caesarCipherEncryptor(string, key):
    # Write your code here.
    msg = ""
    for alpha in string:
        msg += encryption(alpha, key)
    return msg


print(caesarCipherEncryptor('xyz', 2))
