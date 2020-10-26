# -*- coding: utf-8 -*-
import string
import logging

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

# Настройка логгера
logger = logging.getLogger("Caesar")
logger.setLevel(logging.INFO)

# создание log-файла
fh = logging.FileHandler("caesar's.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Создание консольного интерфейса с помощью бесконечного цикла
while True:
    logger.info("Программа запущена")
    print('Выберите действие:', 'Введите 1, если хотите зашифровать сообщение', 'Введите 2, если хотите расшифровать сообщение', 'Введите 3, если хотите выйти из программы', sep = '\n')
    change = input('Ваш выбор: ')

    # Проверка на ввод правильного числа
    if change == '3':
        logger.info("Программа остановлена")
        break
    elif change != '1' and change !='2':
        print('Вы ввели неверный символ. Попробуйте ещё раз')
        logger.info("Пользователь ввёл неверный символ при выборе действия")
        continue

    change = int(change)
    logger.info("Пользователь выбрал действие %s" % change)

    while(True):
        print('\nКакой алфавит используется в сообщении?', 'Введите 1, если русский', 'Введите 2, если латинский', sep = '\n')
        language = input('Ваш выбор: ')

        # Проверка на ввод правильного числа
        if language != '1' and language !='2':
            print('Вы ввели неверный символ. Попробуйте ещё раз')
            logger.info("Пользователь ввёл неверный символ при выборе алфавита")
            continue

        language = int(language)
        logger.info("Пользователь выбрал алфавит %s" % language)
        break

    message = input('Введите строку: ').lower()
    logger.info("Исходная строка: %s" % message)

    while(True):
        key = input('Введите ключ (сдвиг алфавита): ')

        # Проверка на ввод числа
        if key.isdigit() != 1:
            print('Вы ввели неверный символ. Попробуйте ещё раз')
            logger.info("Пользователь ввёл неверный символ при вводе ключа")
            continue

        key = int(key)
        logger.info("Пользователь выбрал сдвиг алфавита %s" % key)
        break

    # Работа с русским алфавитом
    if language == 1:
        if change == 1:
            code_message = code(rus_alphabet, message, key)
        elif change == 2:
            key *= -1
            code_message = code(rus_alphabet, message, key)

    # Работа с латинским алфавитом
    elif language == 2:
        if change == 1:
            code_message = code(eng_alphabet, message, key)
        elif change == 2:
            key *= -1
            code_message = code(eng_alphabet, message, key)

    # Вывод результата
    print('\nРезультат: ' + code_message + '\n')
    logger.info("Результат работы программы: %s" % code_message)
    logger.info("Завершение программы")
