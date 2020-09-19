# -*- coding: utf-8 -*-
import string

# Функция, выполняющая кодирование/декодирование сообщения
def code(alphabet, message, key):
    code_message = ''
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            code_message += alphabet[new_key]
        else:
            code_message += letter
    return code_message

rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
eng_alphabet = string.ascii_lowercase

# Создание консольного интерфейса с помощью бесконечного цикла
while True:
    print('Выберите действие:', 'Введите 1, если хотите зашифровать сообщение', 'Введите 2, если хотите расшифровать сообщение', 'Введите 3, если хотите выйти из программы', sep = '\n')
    change = int(input('Ваш выбор: '))

    if change == 3: break
    elif change != 1 and change !=2:
        print('Вы ввели неверную цифру. Попробуйте ещё раз')
        continue

    print('\nКакой алфавит используется в сообщении?', 'Введите 1, если русский', 'Введите 2, если латинский', sep = '\n')
    language = int(input('Ваш выбор: '))
    if language != 1 and language !=2:
        print('Вы ввели неверную цифру. Попробуйте ещё раз')
        continue

    message = input('Введите строку: ').lower()
    key = int(input('Введите ключ (сдвиг алфавита): '))

    if language == 1:
        if change == 1:
            code_message = code(rus_alphabet, message, key)
        elif change == 2:
            key *= -1
            code_message = code(rus_alphabet, message, key)

    elif language == 2:
        if change == 1:
            code_message = code(eng_alphabet, message, key)
        elif change == 2:
            key *= -1
            code_message = code(eng_alphabet, message, key)

    print('\nРезультат: ' + code_message + '\n')
