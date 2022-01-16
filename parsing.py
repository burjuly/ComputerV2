import re
import solver
import computerv1
import functions

def is_matrix_empty(part):
    if re.findall(r'^([\[]{2})(.*)([\]]{2})$', part)[0][1] == '':
        print('Empty matrix')
        return True
    return False

def analyze_part(part):
    print(f'PART {part}')
    if re.findall(r'^[a-zA-Z]+$', part):
        return('var')
    elif re.findall(r'^[a-zA-Z][/(][-]?[0-9]+[/)]$', part):
        return('func_num')
    elif re.findall(r'^[a-zA-Z][/(][a-zA-Z]+[/)]$', part):
        return('func_var')
    elif re.findall(r'^[-]?[0-9]$', part):
        return('int')
    elif re.findall(r'^[-]?[0-9]+[\.][0-9]+$', part):
        return('float')
    #TODO
    #elif len(re.findall(r'[^0-9a-zA-Z\(\)\+-\*\/^%]', part)) == 0:
    #    return('equation')
    elif re.findall(r'^[\[]{2}.*[\]]{2}$', part):
        if is_matrix_empty(part):
            return
        return('matrix')
    elif len(re.findall(r'[^0-9a-zA-Z\+-|*^\/\(\)%]', part)) == 0:
        return('expression')
    else:
        print('MISTAKES IN THE PART')
        exit()

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

    elif re.findall('^[-]?[0-9]+$', right_side):
        dic_vars.update({left_side: int(right_side)})

    elif re.findall(r'^[-]?[0-9]+[.][0-9]+$', right_side):
        dic_vars.update({left_side: float(right_side)}) 
    

def parse_instruction(instruction, dic_vars):
    print('PARSING')
    parts = instruction.split('=')
    left_side = parts[0]
    right_side = parts[1]

    left = analyze_part(left_side)
    right = analyze_part(right_side)

    print(f'В левой части {left}')
    print(f'В правой части {right}')

    if left is None or right is None:
        return

    if left == 'var':
        if right == 'expression':
            print(f'SOLVE RIGHT PART')
            right_side = solver.solve_expression(right_side, dic_vars)
            print(f'RIGHT SIDE {right_side}')
            update_dic(left_side, right_side, dic_vars)
        else:
            update_dic(left_side, right_side, dic_vars)
    elif left == 'func_var':
        functions.function_of_var(left_side, right_side, right, dic_vars)
    elif left == 'func_num':
        functions.function_of_num(left_side, right_side, right, dic_vars)

        



    else:
        print()
        #solver.solve_expression(left_side, right_side, dic_vars)

