import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    chipher = []
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n=len(alf)
    for i in plaintext:
        index = alf.find(i.upper())
        if index != -1:
            index = (index + shift) % n
            if i.isupper():
                chipher.append(alf[index])
            elif i.islower():
                chipher.append(alf[index].lower())
        else:
            chipher.append(i)
    ciphertext = "".join(chipher)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    chipher = []
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alf)
    for i in ciphertext:
        index = alf.find(i.upper())
        if index != -1:
            index = (index - shift) % n
            if i.isupper():
                chipher.append(alf[index])
            elif i.islower():
                chipher.append(alf[index].lower())
        else:
            chipher.append(i)
    plaintext = "".join(chipher)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift