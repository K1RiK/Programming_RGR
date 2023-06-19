# -*- coding: utf-8 -*-


"""
Функции шифруют и дешифруют текст путем сдвига каждого символа на длину порядкового номера
текщего симола ключа по модулю всего доступного алфавита
"""


def vigener_encode(text: str, key: str) -> str:
    key_lenght = len(key)
    if key_lenght:
        return ''.join([chr((ord(char) + ord(key[index % key_lenght])) % 1114112) for index, char in enumerate(text)])
    return ''


def vigener_decode(text: str, key: str) -> str:
    key_lenght = len(key)
    if key_lenght:
        return ''.join([chr((ord(char) - ord(key[index % key_lenght])) % 1114112) for index, char in enumerate(text)])
    return ''
