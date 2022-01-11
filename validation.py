import re

""" Проверяем что в строке только буквы, цифры, операции """
def check_symbols(instruction):
    for i in instruction:
        if not i.isalnum() and i not in '*/+-()[];:,?^%=':
            print(f'Invalid character found {i}')
            return(0)
    return(1)

def validate_brackets(instruction):
    parts = re.split('=', instruction)
    if len(parts[0]) == 0 or len(parts[1]) == 0:
        print('Empty part')
        return(0)
    for p in parts:
        if p.count('(') != p.count(')') or p.count('[') != p.count(']'):
            print('The number of opening brackets must be equal to the number of closing ')
            return(0)

def validation(instruction):
    if instruction.count('=') != 1:
        print(f'Wrong number of "=" ')
        return(0)
    if check_symbols(instruction) == 0:
        return(0)
    if validate_brackets(instruction) == 0:
        return(0)
    return(1)




