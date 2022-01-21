import re
import solver
import functions
import parsing

def parse_expression_with_functions(left_side, right_side, right_side_type, dic_vars):
    tmp = []
    i = 0
    while i < len(left_side):
        sym = left_side[i]
        if re.search(r'^([a-zA-Z])([\(])([-]?)([0-9]+)([\)])', left_side[i:]):
            func_num = re.search(r'([a-zA-Z])([\(])([-]?)([0-9]+)([\)])', left_side[i:])[0]
            dic_vars = functions.function_of_num(left_side, right_side, right_side_type, dic_vars)
            i += len(func_num)
            tmp.append(dic_vars['i'])
            dic_vars = parsing.del_tmp_vars(dic_vars)
        elif re.search(r'^([a-zA-Z])([\(])([a-zA-Z])([\)])', left_side[i:]):
            func_var = re.search(r'([a-zA-Z])([\(])([a-zA-Z])([\)])', left_side[i:])[0]
            dic_vars = functions.function_of_var(func_var, right_side, right_side_type, dic_vars)
            i += len(func_var)
            tmp.append(dic_vars['i'])
            dic_vars = parsing.del_tmp_vars(dic_vars)
        else:
            tmp.append(sym)
            i += 1
    tmp = "".join(map(str, tmp))
    return(dic_vars, tmp)

def analyze_result(result):
    result = result.replace('--', '+')
    return(result)

def left_side_expression(left_side, right_side, right, dic_vars):
    if re.findall(r'([a-zA-Z])([\(])([0-9a-zA-Z])([\)])', left_side):
        dic_vars, result = parse_expression_with_functions(left_side, right_side, right, dic_vars)
        result = analyze_result(result)
        result = solver.solve_expression(result, dic_vars)
        if result != 'None':
            print(result)
        return(dic_vars)
    result = solver.solve_expression(left_side, dic_vars)
    if result != 'None':
        print(result)
    return(dic_vars)