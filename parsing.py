import re
import solver

def analyze_part(part):
    ''' Левая часть содержит только буквы => это переменная'''
    if len(re.findall(r'[^a-z]', part)) == 0:
        return('var')
    elif len(re.findall(r'[^a-z\(\)]', part)) == 0:
        return('func')
    elif len(re.findall(r'[^0-9]', part)) == 0:
        return('num')
    else:
        return('expression')

''' Левая часть переменная, правая - ? '''       
def right_side_question(left_side, right_side, dic_vars):
    if dic_vars.get(left_side, False):
        res = dic_vars[left_side]
        print(f'{res}')
    else:
        print(f'Variable {right_side} has not  been assigned a value yet ')

def right_side_var(left_side, right_side, dic_vars):
    if dic_vars.get(right_side, False):
        dic_vars.update({left_side: dic_vars[right_side]})
    else:
        print(f'Variable {right_side} has not been assigned a value yet ')

def right_side_float(left_side, right_side, dic_vars):
    if len(re.findall(r'^[-]?[0-9]+[.][0-9]+$', right_side)) != 1:
        print('Wrong right side')
        return False
    return True

def right_side_int(left_side, right_side, dic_vars):
    if len(re.findall(r'^[-]?[0-9]+$', right_side)) != 1:
        print('Wrong right side')
        return False
    return True

def update_dic(left_side, right_side, dic_vars):
    if right_side == '?':
        print('В правой части ?')
        right_side_question(left_side, right_side, dic_vars)

    elif right_side.isalpha():
        print('В правой части переменная')
        right_side_var(left_side, right_side, dic_vars)
       
    elif len(re.findall('[^0-9-\.]', right_side)) > 0:
        print
        print('Wrong right side ')

    else:
        ''' Правая часть float число '''
        if '.' in right_side:
            if right_side_float(left_side, right_side, dic_vars):
                print('В правой части float число')          
                dic_vars.update({left_side: float(right_side)})  
        else:
            if right_side_int(left_side, right_side, dic_vars):
                print('В правой части int число')
                right_side = int(right_side)
                dic_vars.update({left_side: int(right_side)})
        print(right_side)       

def parse_instruction(instruction, dic_vars):
    print('PARSING')

    parts = instruction.split('=')
    left_side = parts[0]
    right_side = parts[1]

    left = analyze_part(left_side)
    right = analyze_part(right_side)

    print(f'В левой части {left}')
    print(f'В правой части {right}')

    if left == 'var':
        if right == 'expression':
            right_side = solver.solve_expression(right_side, dic_vars)
        else:
            update_dic(left_side, right_side, dic_vars)
    elif left == 'func':
        print()
    else:
        print()
        #solver.solve_expression(left_side, right_side, dic_vars)
    
