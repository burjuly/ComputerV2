import re
import solver
import functions
import parsing

def parse_expression_with_functions(left_side, right_side, right_side_type, dic_vars):
    tmp = []
    i = 0
    while i < len(left_side):
        sym = left_side[i]
        print(f'i= {i}')
        print(f'sym = {sym}')
        if re.search(r'^([a-zA-Z])([\(])([-]?)([0-9]+)([\)])', left_side[i:]): # Функция от числа
            print('IN FIRSY IF')
            func_num = re.search(r'([a-zA-Z])([\(])([-]?)([0-9]+)([\)])', left_side[i:])[0]
            print(f'FUNC NUM {func_num}')
            dic_vars = functions.function_of_num(left_side, right_side, right_side_type, dic_vars)
            i += len(func_num)
            #print(f'RESULT = {dic_vars['i']}') 
            tmp.append(dic_vars['i'])
            dic_vars = parsing.del_tmp_vars(dic_vars)
            
        elif re.search(r'^([a-zA-Z])([\(])([a-zA-Z])([\)])', left_side[i:]): # Функция от переменной
            print('IN SECOND ELIF')
            func_var = re.search(r'([a-zA-Z])([\(])([a-zA-Z])([\)])', left_side[i:])[0]
            print(f'FUNC VAR {func_var}')
            dic_vars = functions.function_of_var(func_var, right_side, right_side_type, dic_vars)
            i += len(func_var)
            #print(f'RESULT = {result}') 
            tmp.append(dic_vars['i'])
            dic_vars = parsing.del_tmp_vars(dic_vars)
        else:
            print('IN ELSE')
            tmp.append(sym)
            i += 1
        print(f'i= {i}')
        print(tmp)
        print(dic_vars)
    tmp = "".join(map(str, tmp))
    print(f'RESULT = {tmp}') 
    return(dic_vars, tmp)

def analyze_result(result):
    result = result.replace('--', '+')
    return(result)

def left_side_expression(left_side, right_side, right, dic_vars):
    if re.findall(r'([a-zA-Z])([\(])([0-9a-zA-Z])([\)])', left_side):
        print(f'В выражении есть функции')
        dic_vars, result = parse_expression_with_functions(left_side, right_side, right, dic_vars)
        result = analyze_result(result)
        result = solver.solve_expression(result, dic_vars)
        print(result)
        return(dic_vars)

    result = solver.solve_expression(left_side, dic_vars)
    if result:
        print(result)
    return(dic_vars)