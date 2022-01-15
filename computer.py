import re
import parsing
import validation

def print_dic(dic):
    if len(dic) == 0:
        print('No variable assigned yet')
    for i in dic:
        print(f'{i} = {dic[i]}')

def main():
    dic_vars = {}
    while True:
        print(f'>', end='')
        instruction = input()
        instruction = re.sub(r'\s+', '', instruction)

        if instruction == '':
            print('Empty input... Enter instruction')
            continue

        elif instruction == 'vars':
            print('print vars')
            print_dic(dic_vars)
            continue

        elif instruction == 'exit':
            break

        res_validation = validation.validation(instruction)    
        if res_validation == 0:
            continue
        else:
            parsing.parse_instruction(instruction, dic_vars)

if __name__== "__main__":
    main()