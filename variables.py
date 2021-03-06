import re
import parsing
import solver
import matrix

def left_var(left_side, right_side, right_side_type, dic_vars):
    if right_side_type == 'matrix':
        dic_vars = matrix.right_side_matrix(left_side, right_side, right_side_type, dic_vars)
    elif right_side_type == 'num_mult_matrix':
        dic_vars = matrix.num_mult_matrix(left_side, right_side, right_side_type, dic_vars)
    elif right_side_type ==  'var_mult_matrix':
        dic_vars = matrix.var_mult_matrix(left_side, right_side, right_side_type, dic_vars)
    elif right_side_type == 'complex':
        dic_vars.update({left_side: right_side})
        print(right_side)
    elif right_side_type == 'func_var' or right_side_type == 'func_num':
        print('It is impossible assign a function value to a variable')
    elif left_side == 'i':
        print('It is impossible assign a value for i')
    elif right_side_type == 'question':
        if dic_vars.get(left_side, False):
            res = dic_vars[left_side]
            if re.findall(r'([\[])(.*)([\]])', res):
                res = re.findall(r'([\[])(.*)([\]])', res)[0][1]
            print(res)
        else:
            print(f'Variable {left_side} has not been assigned a value yet ')
    elif right_side_type == 'var':
        if dic_vars.get(right_side, False):
            dic_vars.update({left_side: dic_vars[right_side]})
            res = dic_vars[left_side]
            if re.findall(r'([\[])(.*)([\]])', res):
                res = re.findall(r'([\[])(.*)([\]])', res)[0][1]
            print(res)
        else:
            print(f'Variable {right_side} has not been assigned a value yet ')
    elif right_side_type == 'int':
        dic_vars.update({left_side: right_side})
        print(right_side)
    elif right_side_type == 'float':
        print(right_side)
    elif right_side_type == 'expression':
        right_side = solver.solve_expression(right_side, dic_vars)
        dic_vars.update({left_side: right_side})
        print(right_side)
    elif right_side_type == 'matrix':
        print()
    return(dic_vars)