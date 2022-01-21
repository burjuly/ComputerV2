import re
import complex_num

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
    if b == 0:
        print('Сan\'t divide by zero')
        return
    return(a / b)

def op_remainder(a, b):
    return(a % b)

def op_int_div(a, b):
    return(a // b)

def op_power(a, b):
    return(a ** b)



#TODO добавить парсинг float чисел
def get_tokens(part):
    #print(f'GET TOKEN {part}')
    result = []
    i = 0
    while i < len(part):
        symbol = part[i]
        #TODO float
        if symbol.isalpha():
            symbol = re.search('[a-zA-Z]+', part[i:]).group(0)
            i += len(symbol)
        elif symbol.isdigit():
            if re.search(r'\d+\.\d+', part[i:]):
                symbol = re.search(r'\d+\.\d+', part[i:]).group(0)
            else:
                symbol = re.search('[0-9]+', part[i:]).group(0)
            i += len(symbol)
        elif symbol == '/':
            symbol = re.search('[/]+', part[i:]).group(0)
            i += len(symbol)
        elif symbol in '+, -, *, (, ), %, ^':
            i += 1
        result.append(symbol)
    #print(f'AFTER GET TOKEN {result}')
    return(result)

# Подставляет вместо букв переменные, которые есть в словаре
def substitute_numbers_in_vars(part, dic_vars):
    result = []
    #print(f'ПОДСТАНОВКА ПЕРЕМЕННЫХ {part}')
    for i in part:
        if dic_vars.get(i):
            result.append(str(dic_vars[i]))
        else:
            result.append(i)
    #print(f'RESULT AFTER CHANGE VARS {result}')
    return(result)

def to_rpn(str):
    stack, output_str = [], []
    i = 0
    while i < len(str):
        token = str[i]
        if token.isalpha() or token[0].isdigit():
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
        if 'i' in str(a) or 'i' in str(b):
            return(complex_num.mult_complex(a, b))
        return(op_mult(a, b))
    elif i == '/':
        return(op_div(a, b))
    elif i == '//':
        return(op_int_div(a, b))
    elif i == '%':
        return(op_remainder(a, b))
    elif i == '^':
        if 'i' in str(a):
            return(complex_num.power_for_complex(a, b))
        return(op_power(a, b))
    else:
        print('Inpossible to solve')
        exit()

def to_int_or_float(a, b):
    if 'i' not in a:
        a = float(a) if '.' in a else int(a)
    if 'i' not in b:
        b = float(b) if '.' in b else int(b)
    return(a, b)

def from_rpn(rpn):
    print('IN RPN')
    stack, result = [], []
    for i in rpn:
        if i.isalpha() or i[0].isdigit() or i == 'i':
            stack.append(i)
        elif i in ["+", "-", "*", "//", "/", "%", "^"]:
            b = stack.pop()
            a = stack.pop()
            a, b = to_int_or_float(a, b)
            result = choose_operation(a, b, i)
            stack.append(str(result))
    return(stack[0])

def solve_expression(part, dic_vars):
    part = get_tokens(part)
    tokens = substitute_numbers_in_vars(part, dic_vars)
    #print(f'TOKEN {tokens}')
    
    rpn = to_rpn(tokens)
    #print(f'AFTER RPN {rpn}')
    
    result = from_rpn(rpn)
    #print(f'RESULT IN SOLVERRR {result}')
    return(str(result)) #чтобы в update_dic работал isalpha
    
