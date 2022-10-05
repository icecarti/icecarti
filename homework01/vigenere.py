def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = []
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n =len(alf)
    k = 0
    for i in plaintext:
        index = alf.find(i.upper())
        if index != -1:
            index = (index + alf.find(keyword[k].upper()) ) % n
            if i.isupper():
                ciphertext.append(alf[index])
            elif i.islower():
                ciphertext.append(alf[index].lower())
        else:
            ciphertext.append(i)
        k = k + 1
        if k == len(keyword):
            k = 0
    return "".join(ciphertext)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = []
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alf)
    k = 0
    for i in ciphertext:
        index = alf.find(i.upper())
        if index != -1:
            index = (index - alf.find(keyword[k].upper())) % n
            if i.isupper():
                plaintext.append(alf[index])
            elif i.islower():
                plaintext.append(alf[index].lower())
        else:
            plaintext.append(i)
        k = k + 1
        if k == len(keyword):
            k = 0
    return "".join(plaintext)
