
def power_for_complex(a, b):
    a = a.split('*')
    b = int(b)
    flag = 0
    for i in a:
        if i == 'i':
            if b == 1:
                complex_part = 'i'
                flag = 1
            elif b == 2:
                complex_part = -1
            elif b == 3:
                complex_part = '-i'
                flag = 1
            elif b == 4:
                complex_part = 1
        else:
            rational_part = int(i) ** b
    if flag == 1:
        result = '-' + str(rational_part) + 'i'
    else:
        result = complex_part * rational_part
    return(result)

def mult_complex(a, b):
    print(f'a = {a}')
    print(f'b = {b}')
    if 'i' in str(a):
        return(str(b) + a)
    else:
        return(str(a) + b)
        