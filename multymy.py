# -*- coding: utf-8 -*-
from random import choice

# Крипто словарь
crypto_dict = {'а': 100,
               'б': 101,
               'в': 102,
               'г': 103,
               'д': 104,
               'е': 105,
               'ж': 106,
               'з': 107,
               'и': 108,
               'й': 109,
               'к': 110,
               'л': 111,
               'м': 112,
               'н': 113,
               'о': 114,
               'п': 115,
               'р': 116,
               'с': 117,
               'т': 118,
               'у': 119,
               'ф': 120,
               'х': 121,
               'ц': 122,
               'ч': 123,
               'ш': 124,
               'щ': 125,
               'ъ': 126,
               'ы': 127,
               'ь': 128,
               'э': 129,
               'ю': 130,
               'я': 131,
               'А': 132,
               'Б': 133,
               'В': 134,
               'Г': 135,
               'Д': 136,
               'Е': 137,
               'Ж': 138,
               'З': 139,
               '?': 140,
               'Й': 141,
               'К': 142,
               'Л': 143,
               'М': 144,
               'Н': 145,
               'О': 146,
               'П': 147,
               'Р': 148,
               'С': 149,
               'Т': 150,
               'У': 151,
               'Ф': 152,
               'Х': 153,
               'Ц': 154,
               'Ч': 155,
               'Ш': 156,
               'Щ': 157,
               'Ъ': 158,
               'Ы': 159,
               'Ь': 160,
               'Э': 161,
               'Ю': 162,
               'Я': 163,
               '!': 164,
               '.': 165,
               ',': 166,
               '/': 167,
               '1': 168,
               '2': 169,
               '3': 170,
               '4': 171,
               '5': 172,
               '6': 173,
               '7': 174,
               '8': 175,
               '9': 176,
               '0': 177,
               '-': 178,
               '+': 179,
               '_': 180,
               '=': 181,
               '@': 182,
               '*': 183,
               '(': 184,
               ')': 185,
               '№': 186,
               ':': 187,
               ';': 188,
               '"': 189,
               'A': 190,
               'B': 191,
               'C': 192,
               'D': 193,
               'E': 194,
               'F': 195,
               'G': 196,
               'H': 197,
               'I': 198,
               'J': 199,
               'K': 200,
               'L': 201,
               'M': 202,
               'N': 203,
               'O': 204,
               'P': 205,
               'Q': 206,
               'R': 207,
               'S': 208,
               'T': 209,
               'U': 210,
               'V': 211,
               'W': 212,
               'X': 213,
               'Y': 214,
               'Z': 215,
               '[': 216,
               ']': 217,
               '`': 218,
               'a': 219,
               'b': 220,
               'c': 221,
               'd': 222,
               'e': 223,
               'f': 224,
               'g': 225,
               'h': 226,
               'i': 227,
               'j': 228,
               'k': 229,
               'l': 230,
               'm': 231,
               'n': 232,
               'o': 233,
               'p': 234,
               'q': 235,
               'r': 236,
               's': 237,
               't': 238,
               'u': 239,
               'v': 240,
               'w': 241,
               'x': 242,
               'y': 243,
               'z': 244,
               '{': 245,
               '#': 246,
               '$': 247,
               '%': 248,
               '^': 249,
               '&': 250,
               '}': 251,
               '<': 252,
               '>': 253,
               ' ': 254,
               "'": 255,
               '\\': 256,
               '|': 257,
               '\n': 258,
               'И': 259}

# Словарь для перевода
num_to_char = {'0': ('k', 'l', ';', ':', 'B', 'N', 'И'),
               '1': ('q', 'w', 'e', 'r', 'E', 'L', 'Б'),
               '2': ('a', 's', 'd', 'f', 'Q', 'W', 'F'),
               '3': ('z', 'x', 'c', 'v', 'S', 'D', 'U'),
               '4': ('t', 'y', 'u', 'i', 'Z', 'X', 'C'),
               '5': ('g', 'h', 'j', 'G', 'T', 'Y', 'K'),
               '6': ('b', 'n', 'm', ',', 'H', 'J', 'Г'),
               '7': ('.', '>', '?', '/', 'I', 'R', 'К'),
               '8': (']', '}', '=', '+', 'V', 'M', 'Ъ'),
               '9': ('A', '_', '{', '[', ')', '(', 'Ь')}

translate_string = ''.join([''.join(_) for _ in tuple(num_to_char.values())])


def crypto(text: str, key: int) -> str:
    crypto_list = ''
    key = key + (key >> 7)
    for char in text:
        if char not in crypto_dict.keys():
            return f'Ошибка шифрования, символа {char} нет в словаре!\n\
                    \rПопробуйте другой символ или добавьте символ в словарь'
        crypto_list += str(key * crypto_dict[char])
    output = ''.join(map(lambda s: choice(num_to_char[s]), crypto_list))
    return output


def decrypto(text: str, key: int) -> str:
    if not text:
        return ''
    for char in text:
        if char not in translate_string:
            return f'Ошибка дешифровки, символа {char} нет в словаре для перевода!\n'
    for keyword, value in num_to_char.items():
        for char in value:
            text = text.replace(char, keyword)
    crypto_list, decrypto_list = text, ''
    start, end = 0, 2
    select = int(crypto_list[start:end])
    key = key + (key >> 7)
    for _ in crypto_list:
        try:
            if not select % key and len(str(select // key)) == 3:
                start, end = end, end + 2
                for keyword, value in crypto_dict.items():
                    if value == select / key:
                        decrypto_list += keyword
            else:
                end += 1
            select = int(crypto_list[start:end])
        except:
            break
    return ''.join(decrypto_list)
