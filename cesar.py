# -*- coding: utf-8 -*-
def cesar_encode(text: str, key: int) -> str:
    return ''.join([chr((ord(c) + key) % 1114112) for c in text])


def cesar_decode(text: str, key: int) -> str:
    return ''.join([chr((ord(c) - key) % 1114112) for c in text])
