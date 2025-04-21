with open("input.txt", "r") as f: lines = f.read().split("\n")

map = {}
for i, line in enumerate(lines):
    result, expression =  line.split("=")
    map[result] = f"({i})"
    op_found = False
    for operator in ["+", "-", "*", "/"]:
        if operator in expression:
            op1, op2 =  expression.split(operator)
            op_found = True
            print((i, operator, map.get(op1, op1), map.get(op2, op2)))
    if not op_found:
        print((i, "=", map.get(expression, expression), "-"))


print(map)