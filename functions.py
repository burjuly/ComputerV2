import re
import solver
import parsing

# Проверяем что в правой части функции тот же аргумент, что в левой
def validate_function(left_side, right_side, dic_vars):
    arg = re.findall(r'([a-zA-Z]+)([\(])([a-zA-Z]+)([\)])', left_side)[0][2]
    tokens = solver.get_tokens(right_side)
    tokens = solver.substitute_numbers_in_vars(right_side, dic_vars)
    vars = re.findall(r'[a-zA-Z]', right_side)
    for i in vars:
        if i not in arg:
            print(f'The left side can only contain a variable {i}, numbers and operations')
            return
    return True

def function_of_var(left_side, right_side, right_side_type, dic_vars):
    if validate_function(left_side, right_side, dic_vars) is None:
        return
    #TODO Solve right side 
    if right_side_type == 'var':
        print()
    dic_vars.update({left_side: right_side})

def function_of_num(left_side, right_side, right_side_type, dic_vars):
    # Узнаем от какого аргумента рассчитать функцию
    tmp = re.findall(r'([a-zA-Z]+)([\(])([0-9]+)([\)])', left_side)[0]
    func_name = tmp[0]
    arg = tmp[2]
    

    print(f'РАССЧИТАТЬ ЗНАЧЕНИЕ ФУНКЦИИ ОТ АРГУМЕНТА: {arg}')
    func_value = ''
    for k in dic_vars:
        if parsing.analyze_part(k) == 'func_var': #тип ключа - функция
            if k.split('(')[0] == func_name:
                func_value = dic_vars[k]
                break
        if func_value == '':
            print('Функция не найдена в словаре. Невозможно рассчитать значение от неизвестной функции')
            return
    print(f'FUNCTION VALUE {func_value}')
