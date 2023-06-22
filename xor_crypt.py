# -*- coding: utf-8 -*-
def encrypt_xor(text: str, key: str) -> str:
    """ XOR шифрование путем побитовой операции над каждым символом входного текста символом ключа """
    key_lenght = len(key)
    if key_lenght:
        return ''.join([chr(((ord(char) - 32 ^ ord(key[index % key_lenght])) + 32) % 1114112) for index, char in enumerate(text)])
    return ''
