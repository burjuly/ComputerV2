import re

def is_matrix_empty(part):
    if re.findall(r'^([\[]{2})(.*)([\]]{2})$', part)[0][1] == '':
        print('Empty matrix')
        return True
    return False
    
def check_symbols(instruction):
    if not instruction.isascii():
        print('Only ASCII characters are allowed')
        return(0)     
    for i in instruction:
        if not i.isalnum() and i not in '*/+-()[];:.,?^%=':
            print(f'Invalid character found {i}')
            return(0)
    return(1)

def validate_brackets(instruction):
    parts = re.split('=', instruction)
    if len(parts[0]) == 0 or len(parts[1]) == 0:
        print('Invalid input. Empty part')
        return(0)
    for p in parts:
        if p.count('(') != p.count(')') or p.count('[') != p.count(']'):
            print('The number of opening brackets must be equal to the number of closing ')
            return(0)
    return(1)

def are_signs_placed_correctly(instruction):
    parts = re.split('=', instruction)
    for p in parts:
        if len(re.findall(r'[+-][+-]', p)):
            print('The signs in the expression are placed incorrectly')
            return(0)
    return(1)

def validation(instruction):
    if check_symbols(instruction) == 0:
        return(0)
    if instruction.count('=') != 1:
        print(f'Wrong number of "=" ')
        return(0)
    if validate_brackets(instruction) == 0:
        return(0)
    if are_signs_placed_correctly(instruction) == 0:
        return(0)
    return(1)




