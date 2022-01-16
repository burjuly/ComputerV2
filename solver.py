import re

OPERATIONS = {
    "^": 3,
    "*": 2,
    "/": 2,
    "//": 2,
    "%": 2,
    "+": 1,
    "-": 1 
    }

def op_add(a, b):
    return(a + b)

def op_sub(a, b):
    return(a - b)

def op_mult(a, b):
    return(a * b)

def op_div(a, b):
    return(a / b)

def op_remainder(a, b):
    return(a % b)

def op_int_div(a, b):
    return(a // b)

def op_power(a, b):
    return(a ** b)

#TODO добавить парсинг float чисел
def get_tokens(part):
    print(f'GET TOKEN {part}')
    result = []
    i = 0
    while i < len(part):
        symbol = part[i]
        if symbol.isalpha():
            symbol = re.search('[a-zA-Z]+', part[i:]).group(0)
            i += len(symbol)
        elif symbol.isdigit():
            symbol = re.search('[0-9]+', part[i:]).group(0)
            i += len(symbol)
            #symbol = int(symbol)
        elif symbol in '+, -, *, /, (, ), %, ^':
            i += 1
        result.append(symbol)
    print(f'AFTER GET TOKEN {result}')
    return(result)

# Подставляет вместо букв переменные, которые есть в словаре
def substitute_numbers_in_vars(part, dic_vars):
    result = []
    print(f'ПОДСТАНОВКА ПЕРЕМЕННЫХ {part}')
    for i in part:
        if dic_vars.get(i):
            result.append(str(dic_vars[i]))
        else:
            result.append(i)
    print(f'RESULT AFTER CHANGE VARS {result}')
    return(result)

def to_rpn(str):
    stack, output_str = [], []
    i = 0
    while i < len(str):
        token = str[i]
        if token.isalpha() or token.isnumeric():
            output_str.append(token)
        elif token == '(':
            stack.append(token)
        elif str[i] == ')':
            while stack[-1] != '(':
                output_str.append(stack.pop())
            stack.pop()
        elif token in OPERATIONS:
            while len(stack):
                if stack[-1] == '(':
                    break
                elif OPERATIONS[stack[-1]] >= OPERATIONS[token]:
                    output_str.append(stack.pop())
                else:
                    break
            stack.append(token)
        i += 1
    while len(stack):
        output_str.append(stack.pop())    
    return(output_str)

def choose_operation(a, b, i):
    if i == '+':
        return(op_add(a, b))
    elif i == '-':
        return(op_sub(a, b))
    elif i == '*':
        return(op_mult(a, b))
    elif i == '/':
        return(op_div(a, b))
    elif i == '//':
        return(op_int_div(a, b))
    elif i == '%':
        return(op_remainder(a, b))
    elif i == '^':
        return(op_power(a, b))
    else:
        print('Inpossible to solve')
        exit()


def from_rpn(rpn):
    print('IN RPN')
    stack, result = [], []

    for i in rpn:
        if i.isalpha() or i.isdigit():
            stack.append(i)
        elif i in ["+", "-", "*", "//", "/", "%", "^"]:
            #Проверить что из стека достаем число
            #Буква ?
            b = int(stack.pop())
            a = int(stack.pop())
            result = choose_operation(a, b, i)
            stack.append(result)
    return(stack[0])

''' 
1. Разбиваем на токены
2. Заменяем переменные на числа (если есть в словаре)
3. Переводим в rpn
4. Решаем rpn '''
def solve_expression(part, dic_vars):
    print('SOLVER')
    part = get_tokens(part)
    print(f'PART {part}')

    tokens = substitute_numbers_in_vars(part, dic_vars)
    print(f'TOKEN {tokens}')
    
    rpn = to_rpn(tokens)
    print(rpn)
    
    result = from_rpn(rpn)
    print(result)
    return(str(result)) #чтобы в update_dic работал isalpha
    
