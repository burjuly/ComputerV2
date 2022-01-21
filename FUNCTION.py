import re
import solver
import parsing

def validate_function(left_side, right_side, dic_vars):
    if re.findall(r'^([a-zA-Z])([\*])(\[)(.*)(\])$', right_side):
        print(right_side)
        dic_vars.update({left_side: right_side})
        return(dic_vars)
    arg = re.findall(r'([a-zA-Z]+)([\(])([a-zA-Z]+)([\)])', left_side)[0][2]
    tokens = solver.get_tokens(right_side)
    tokens = solver.substitute_numbers_in_vars(right_side, dic_vars)
    vars = re.findall(r'[a-zA-Z]', right_side)
    for i in vars:
        if i not in arg and i != 'i':
            print(f'The left side can only contain a variable {arg}, numbers and operations')
            return
    return True

def function_of_var(left_side, right_side, right_side_type, dic_vars):
    if right_side_type == 'question':
        if left_side in dic_vars: # Для x = 2  f(x) = ?
            print('YESSS')
            right_side = dic_vars[left_side]
            result = solver.solve_expression(right_side, dic_vars)
            if result:
                print(result)
            return(dic_vars)
        else: # Для f(x) = x+2    p = 3    f(p) = ?
            tmp = re.split(r'[\(|\)]', left_side)
            func_name = tmp[0]
            func_arg = tmp[1]

            func_value, func_var = get_function_from_dic(dic_vars, func_name)
            if not func_value:
                print('Function not found in dictionary. Unable to calculate value from unknown function')
                return dic_vars

            print(f'FUNC VAR {func_var}')
            print(f'FUNC VALUE {func_value}')
            print(f'DIC {dic_vars}')
            print(f'FUNC ARG {func_arg}')

            dic_vars.update({func_var: dic_vars[func_arg] })
            result = solver.solve_expression(func_value, dic_vars)
            dic_vars.pop(func_var)
            if result:
                print(result)
            return(dic_vars)
    elif right_side_type == 'expression':
        right_side = solver.substitute_numbers_in_vars(right_side, dic_vars)
        right_side = "".join(map(str,right_side))
        if validate_function(left_side, right_side, dic_vars) is None:
            return(dic_vars)
        dic_vars.update({left_side: right_side})
    return(dic_vars)

'''       
    if dic_vars.get(left_side) is None:
        print('This function has not yet been assigned a value')
        return(dic_vars)
    else:
        dic_vars = function_of_num(left_side, right_side, right_side_type, dic_vars)
    
    right_side = solver.substitute_numbers_in_vars(right_side, dic_vars)
    right_side = "".join(map(str,right_side))
    print(f'RIGHT AFTER {right_side}')
    if validate_function(left_side, right_side, dic_vars) is None:
        return
    #TODO Solve right side 
    if right_side_type == 'var':
        print()
    dic_vars.update({left_side: right_side})
    return(dic_vars)
'''

def get_function_from_dic(dic_vars, func_name ):
    for k in dic_vars:
        if parsing.analyze_part(k) == 'func_var':
            function_in_dic = re.split(r'[\(|\)]', k)
            if function_in_dic[0] == func_name:
                func_value = dic_vars[k]
                func_var = function_in_dic[1]
                return(func_value, func_var)
    return None, None

def function_of_num(left_side, right_side, right_side_type, dic_vars):
    tmp = re.split(r'[\(|\)]', left_side)
    func_name = tmp[0]
    arg = tmp[1]
    if arg.isalpha():
        left_side = solver.substitute_numbers_in_vars(left_side, dic_vars)
        left_side = "".join(map(str, left_side))
    func_value, func_var = get_function_from_dic(dic_vars, func_name )
    if not func_value:
        print('Function not found in dictionary. Unable to calculate value from unknown function')
        return
    print(f'FUNCTION VALUE {func_value}')
    print(f'FUNCTION VAR {func_var}')
    dic_vars.update({func_var: arg})
    result = solver.solve_expression(func_value, dic_vars)
    dic_vars.pop(func_var)
    print(f'{left_side} = {result}')
    return(dic_vars, result)
