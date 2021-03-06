import re
import solver
import computerv1
import functions
import variables
import validation
import expression
import matrix
import plots

def analyze_part(part):
    if part == '?':
        return('question')
    elif re.findall('plot', part):
        return('plot')
    elif re.findall(r'^[a-zA-Z]+$', part):
        return('var')
    elif re.findall(r'^[a-zA-Z][/(][-]?[0-9]+[/)]$', part):
        return('func_num')
    elif re.findall(r'^[a-zA-Z][/(][a-zA-Z]+[/)]$', part):
        return('func_var')
    elif re.findall(r'^[-]?[0-9]+$', part):
        return('int')
    elif re.findall(r'^[-]?[0-9]+[\.][0-9]+$', part):
        return('float')
    elif 'i' in part:
        return('complex')
    elif re.findall(r'^(\d+)([\*])(\[)(.*)(\])$', part):
        return('num_mult_matrix')
    elif re.findall(r'^([a-zA-Z])([\*])(\[)(.*)(\])$', part):
        return('var_mult_matrix')
    elif re.findall(r'^([\w])([\*]{2})([\w])$', part):
        return('matrix_mult_matrix')
    elif re.findall(r'^[a-zA-Z][\?]$', part):
        return('var_question')
    elif re.findall(r'^[\[]{2}.*[\]]{2}$', part):
        if validation.is_matrix_empty(part):
            return
        return('matrix')
    elif len(re.findall(r'[^0-9a-zA-Z\+-|*^\/\(\)%]', part)) == 0:
        return('expression')

    else:
        print('MISTAKES IN THE PART')
        exit()

def del_tmp_vars(dic_vars):
    if 'i' in dic_vars:
        dic_vars.pop('i')
    return(dic_vars)

def parse_instruction(instruction, dic_vars):
    parts = instruction.split('=')
    left_side = parts[0]
    right_side = parts[1]
    left = analyze_part(left_side)
    right = analyze_part(right_side)
    if left is None or right is None:
        return
    if left == 'var':
        dic_vars = variables.left_var(left_side, right_side, right, dic_vars) 
    elif left == 'func_var':
        if right == 'var_question':
            dic_vars = computerv1.check_eqution(left_side, right_side, right, dic_vars)
        else:
            dic_vars = functions.function_of_var(left_side, right_side, right, dic_vars)
            dic_vars = del_tmp_vars(dic_vars)
    elif left == 'func_num':
        dic_vars = functions.function_of_num(left_side, right_side, right, dic_vars)
        dic_vars = del_tmp_vars(dic_vars)
    elif left == 'expression':
        dic_vars = expression.left_side_expression(left_side, right_side, right, dic_vars)
    elif left == 'matrix':
        dic_vars = matrix.left_side_matrix(left_side, right_side, right, dic_vars)
    elif left == 'matrix_mult_matrix':
        dic_vars = matrix.matrix_mult_matrix(left_side, right_side, right, dic_vars)
    elif left == 'int':
        if right == 'int':
            print('Impossible assign a number to another number')
    elif left == 'plot':
        plots.paint_plot(left_side, right_side, right, dic_vars)
    else:
        print('Error in instruction')
    return(dic_vars)

