import re
import solver
import functions

def left_side_expression(left_side, right_side, right, dic_vars):
    result = solver.solve_expression(left_side, dic_vars)
    if result:
        print(result)
    
    if re.findall(r'[a-zA-Z]\([-]?[\d+|a-zA-Z]\)', left_side):
        print()
        #f(3) - f(p) + 2 = ?
        #functions = re.findall(r'([a-zA-Z])\(([-]?[\d+|a-zA-Z]\)', left_side)
        #for f in functions:
            

    return(dic_vars)