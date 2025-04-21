with open("q.txt", "r") as f: lines = f.read().split("\n")

for line in lines:
    result, expression = line.split("=")
    op_found = False
    for operator in ["+", "-", "*", "/"]:
        if operator in expression:
            op1, op2 = expression.split(operator)
            op_found = True
            print((operator, op1, op2, result))
    if not op_found:
        print(("=", expression, "-", result))