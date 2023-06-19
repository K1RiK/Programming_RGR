# -*- coding: utf-8 -*-


"""
Функции шифруют и дешифруют текст путем сдвига каждого символа
на длину ключа по модую всего доступного алфавита
"""


def cesar_encode(text: str, key: int) -> str:
    return ''.join([chr((ord(char) + key) % 1114112) for char in text])


def cesar_decode(text: str, key: int) -> str:
    return ''.join([chr((ord(char) - key) % 1114112) for char in text])
