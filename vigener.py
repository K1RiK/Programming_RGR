# -*- coding: utf-8 -*-
def vigener_encode(text: str, key: str) -> str:
    key_lenght = len(key)
    if not key_lenght:
        return ''
    return ''.join([chr((ord(c) + ord(key[i % key_lenght])) % 1114112) for i, c in enumerate(text)])


def vigener_decode(text: str, key: str) -> str:
    key_lenght = len(key)
    if not key_lenght:
        return ''
    return ''.join([chr((ord(c) - ord(key[i % key_lenght])) % 1114112) for i, c in enumerate(text)])


def check_cesar(itext: str, otext: str, key: int, cmd: bool) -> bool:
    return (cmd and vigener_encode(itext, key) == otext) or (not cmd and vigener_encode(otext, key) == itext)
