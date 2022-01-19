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
    right_side = re.findall(r'^(\d+)([\*])(\[)(.*)(\])$', right_side)[0]
    num = int(right_side[0])
    matrix = right_side[3]
    matrix = matrix.split(';')
    count_rows = len(matrix)
    i = 0
    new_matrix = []
    while i < count_rows:
        tmp = matrix[i]
        new_row = []
        for t in tmp:
            if t.isdigit():
                new_row.append(int(t) * num)
            else:
                new_row.append(t)
        new_matrix.append(new_row)
        i += 1

    result = ''
    for row in new_matrix:
        r = "".join(map(str,row))
        print(r)
        result += r
    result = '[' + r + ']'
    dic_vars.update({left_side: result})
    return(dic_vars)

def var_mult_matrix(left_side, right_side, right_side_type, dic_vars):
    result = []
    for i in right_side:
        if i.isalpha():
            result.append(dic_vars[i])
        else:
            result.append(i)

    result = "".join(map(str,result)) 
    print(f"RESULT {result}")
    return(num_mult_matrix(left_side, result, right_side_type, dic_vars))