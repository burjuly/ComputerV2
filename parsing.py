import re
import solver
import computerv1
import functions
import variables
import validation
import expression
import matrix

def analyze_part(part):
    print(f'PART {part}')
    if part == '?':
        return('question')
    elif re.findall(r'^[a-zA-Z]+$', part):
        return('var')
    elif re.findall(r'^[a-zA-Z][/(][-]?[0-9]+[/)]$', part):
        return('func_num')
    elif re.findall(r'^[a-zA-Z][/(][a-zA-Z]+[/)]$', part):
        return('func_var')
    elif re.findall(r'^[-]?[0-9]$', part):
        return('int')
    elif re.findall(r'^[-]?[0-9]+[\.][0-9]+$', part):
        return('float')
    #TODO equation
    #elif len(re.findall(r'[^0-9a-zA-Z\(\)\+-\*\/^%]', part)) == 0:
    #    return('equation')
    elif re.findall(r'^[\[]{2}.*[\]]{2}$', part):
        if validation.is_matrix_empty(part):
            return
        return('matrix')
    elif len(re.findall(r'[^0-9a-zA-Z\+-|*^\/\(\)%]', part)) == 0:
        return('expression')
    else:
        print('MISTAKES IN THE PART')
        exit()

'''
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
'''

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
    
    #TODO возращать обновленный словарь
    if left == 'var':
        dic_vars = variables.left_var(left_side, right_side, right, dic_vars) 
    elif left == 'func_var':
        dic_vars = functions.function_of_var(left_side, right_side, right, dic_vars)
    elif left == 'func_num':
        dic_vars = functions.function_of_num(left_side, right_side, right, dic_vars)
    elif left == 'expression':
        dic_vars = expression.left_side_expression(left_side, right_side, right, dic_vars)
    elif left == 'matrix':
        dic_vars = matrix.left_side_matrix(left_side, right_side, right, dic_vars)

    else:
        print()
        #solver.solve_expression(left_side, right_side, dic_vars)
    return(dic_vars)

