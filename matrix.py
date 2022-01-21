import re
import solver

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
    result = "".join(map(str, result)) 
    print(f"RESULT {result}")
    return(num_mult_matrix(left_side, result, right_side_type, dic_vars))

def prepare_matrix(matrix):
    matrix = matrix[1:-1].split(';')
    result = []
    for i in matrix:
        row = []
        tmp = i[1:-1].split(',')
        for t in tmp:
            row.append(int(t))
        result.append(row)
    return(result)

def matrix_mult_matrix(left_side, right_side, right, dic_vars):
    left_side = solver.substitute_numbers_in_vars(left_side, dic_vars)
    A = left_side[0]
    B = left_side[-1]
    
    A = prepare_matrix(A)
    B = prepare_matrix(B)

    n = len(A)
    ans = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = sum((A[i][v] * B[v][j] for v in range(n)))

    for a in ans:
        print(a)
    return(dic_vars)