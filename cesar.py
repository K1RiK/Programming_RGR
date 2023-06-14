# -*- coding: utf-8 -*-
def cesar_encode(text: str, key: int) -> str:
    return ''.join([chr((ord(c) + key) % 1114112) for c in text])


def cesar_decode(text: str, key: int) -> str:
    return ''.join([chr((ord(c) - key) % 1114112) for c in text])


def check_cesar(itext: str, otext: str, key: int, cmd: bool) -> bool:
    return (cmd and cesar_encode(itext, key) == otext) or (not cmd and cesar_encode(otext, key) == itext)
