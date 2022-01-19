import re

def print_matrix(matrix):
    matrix = matrix.split(';')
    for m in matrix:
        print(m)

def left_side_matrix(left_side, right_side, right, dic_vars):
    print()

def right_side_matrix(left_side, right_side, right_side_type, dic_vars):
    dic_vars.update({left_side: right_side})
    right_side = re.findall(r'(\[)(.*)(\])', right_side)[0][1]
    print_matrix(right_side)
    return(dic_vars)

def num_mult_matrix(left_side, right_side, right_side_type, dic_vars):
    
    #В словарь уже перемноженный результат
    dic_vars.update({left_side: right_side})
    return(dic_vars)