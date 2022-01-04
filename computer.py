import re
import parsing as pars
import validation as valid

def print_dic(dic):
    for i in dic:
        print(f'{i} : {dic[i]}')

def main():
    dic_vars, dic_func  = {}, {}
    while True:
        print(f'>', end='')
        instruction = input()

        if instruction == '':
            print('Empty input... Enter instruction')

        elif instruction == 'vars':
            print_dic(dic_vars)

        elif instruction == 'func':
            print_dic(dic_func)

        elif instruction == 'exit':
            break
        else:
            print('validation')
            valid.validation(instruction)
            pars.parse_instruction(instruction)

if __name__== "__main__":
    main()