# -*- coding: utf-8 -*-
from random import choice

# Крипто словарь
LETTERS = ''.join([chr(i) for i in range(32, 10000)]) + '\t\n\r'
CRYPTO_DICT = {key: value + 10000 for value, key in enumerate(LETTERS)}

# Словарь для перевода
NUM_TO_CHAR = {str(index): value for index, value in enumerate([LETTERS[26::][_*12:(_+1)*12] for _ in range(5)] +
                                                               [LETTERS[1008::][_*12:(_+1)*12] for _ in range(5)])}

TRANSLATE_STRING = ''.join([''.join(_) for _ in tuple(NUM_TO_CHAR.values())])


def crypto(text: str, key: int) -> str:
    crypto_list = ''
    key = key + (key >> 7)
    for char in text:
        if char not in LETTERS:
            return f'Ошибка шифрования, символа {char} нет в словаре!\n\
                    \rПопробуйте другой символ или добавьте символ в словарь'
        crypto_list += str(key * CRYPTO_DICT[char])
    output = ''.join(map(lambda s: choice(NUM_TO_CHAR[s]), crypto_list))
    return output


def decrypto(text: str, key: int) -> str:
    if not text:
        return ''
    for char in text:
        if char not in TRANSLATE_STRING:
            return f'Ошибка дешифровки, символа {char} нет в словаре для перевода!\n'
    for keyword, value in NUM_TO_CHAR.items():
        for char in value:
            text = text.replace(char, keyword)
    result = ''
    start, end = 0, 4
    select = int(text[start:end])
    key = key + (key >> 7)
    end_point = len(text) + 1
    while end < end_point:
        try:
            if not select % key and len(str(select // key)) == 5:
                start, end = end, end + 4
                result += LETTERS[(select // key) - 10000]
            else:
                end += 1
            select = int(text[start:end])
        except:
            break
    return result
