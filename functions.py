import re
import solver
import parsing

def validate_function(left_side, right_side, dic_vars):
    arg = re.findall(r'([a-zA-Z]+)([\(])([a-zA-Z]+)([\)])', left_side)[0][2]
    tokens = solver.get_tokens(right_side)
    tokens = solver.substitute_numbers_in_vars(right_side, dic_vars)
    vars = re.findall(r'[a-zA-Z]', right_side)
    for i in vars:
        if i not in arg and i != 'i':
            print(f'The left side can only contain a variable {arg}, numbers and operations')
            return None
    return True

def is_right_side_matrix(left_side, right_side, right_side_type, dic_vars):
    right_side = solver.substitute_numbers_in_vars(right_side, dic_vars)
    right_side = "".join(map(str,right_side))
    if re.findall(r'^([a-zA-Z])([\*])(\[)(.*)(\])$', right_side): 
        print(right_side)
        dic_vars.update({left_side: right_side})
        return(dic_vars)
    return None

def function_of_var(left_side, right_side, right_side_type, dic_vars, print_result=True):
    if right_side_type == 'complex':
        dic_vars.update({left_side: right_side})
        print(f'{left_side} = {right_side}' )
        return(dic_vars)
    elif right_side_type == 'expression':
        new_dic = is_right_side_matrix(left_side, right_side, right_side_type, dic_vars)
        if new_dic:
            return(new_dic)
        if validate_function(left_side, right_side, dic_vars) is None:
            return(dic_vars)
        dic_vars.update({left_side: right_side})
        print(f'{left_side} = {right_side}' )
        return(dic_vars)
    elif right_side_type == 'question':
        tmp = re.split(r'[\(|\)]', left_side)
        func_name = tmp[0]
        func_arg = tmp[1]
        func_value, func_var = get_function_from_dic(dic_vars, func_name)
        if func_value is None:
            print('Function not found in dictionary. Unable to calculate value from unknown function')
            return(dic_vars)
        dic_vars.update({func_var: dic_vars[func_arg] })
        result = solver.solve_expression(func_value, dic_vars)
        dic_vars.pop(func_var)
        dic_vars.update({'i': result })
        if result and print_result:
            print(result)
        return(dic_vars)


def get_function_from_dic(dic_vars, func_name ):
    for k in dic_vars:
        if parsing.analyze_part(k) == 'func_var':
            function_in_dic = re.split(r'[\(|\)]', k)
            if function_in_dic[0] == func_name:
                func_value = dic_vars[k]
                func_var = function_in_dic[1]
                return(func_value, func_var)
    return None, None

def function_of_num(left_side, right_side, right_side_type, dic_vars, print_result=True):
    tmp = re.split(r'[\(|\)]', left_side)
    func_name = tmp[0]
    arg = tmp[1]
    if arg.isalpha():
        left_side = solver.substitute_numbers_in_vars(left_side, dic_vars)
        left_side = "".join(map(str, left_side))
    func_value, func_var = get_function_from_dic(dic_vars, func_name )
    if not func_value:
        print('Function not found in dictionary. Unable to calculate value from unknown function')
        return(dic_vars)
    dic_vars.update({func_var: arg})
    result = solver.solve_expression(func_value, dic_vars)
    dic_vars.pop(func_var)
    dic_vars.update({'i': result })
    if print_result:
        print(f'{left_side} = {result}')
    return(dic_vars)
