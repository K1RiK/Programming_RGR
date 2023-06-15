# -*- coding: utf-8 -*-
def encrypt_xor(text: str, key: str) -> str:
    key_lenght = len(key)
    return '' if not key_lenght else ''.join([chr((ord(c) ^ ord(key[i % key_lenght])) % 1114112) for i, c in enumerate(text)])
