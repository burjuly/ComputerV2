import re

""" Убираем пробелы и валидируем количество равно"""
def preparation(instruction):
    instruction = re.sub(r'\s+', '', instruction)
    if instruction.count('=') != 1:
        print(f'Wrong number of "=" ')
        exit()

""" Проверяем что в строке только буквы, цифры, операции """
def check_symbols(instruction):
    for i in instruction:
        if not i.isalnum() and i not in '*/+-()[];:?^%':
            print(f'Invalid character found {i}')
            exit()

def validate_parts(parts):
    left_part = parts[0]
    right_part = parts[1]

    for p in left_part:
        re.findall('[]')

def validation(instruction):
    instruction = preparation(instruction)
    check_symbols(instruction)
    parts = re.split('=', instruction)
    validate_parts(parts)





