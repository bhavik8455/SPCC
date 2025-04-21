with open('input.txt','r') as f:
    lines = f.read().split('\n')

for line in lines:
    result,expression = line.split('=')
    op_found = False
    for operator in ['*','-','+','/']:
        if operator in expression:
            op1,op2 = expression.split(operator)
            op_found = True
            print((operator, op1, op2, result))
    if op_found == False:
        print((' = ', op1, op2, result))