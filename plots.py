import re
import matplotlib.pyplot as plt
import solver

def paint_plot(left_side, right_side, right, dic_vars):
    print(1)
    func = re.findall(r'([\(])(.*)([\)])', left_side)[0][1]
    print(func)
    if func in dic_vars:
        value = dic_vars[func]
    else:
        print('It is impossible to build a graph from an unknown function')
        return
    x = list(range(1, 50, 1))
    y = []
    for i in x:
        dic_vars.update({'x': int(i)})
        result = solver.solve_expression(value, dic_vars)
        dic_vars.pop('x')
        y.append(int(result))

    plt.plot(x, y)
    plt.show()

    



