import re
def is_constant(e):
    try: return eval(e) or True
    except: return False
with open("source.txt", "r") as f: lines = f.read().split("\n")
copies, expressions = {}, {}
for line in lines:
    lhs, rhs = line.split("=")
    if is_constant(rhs):
        print(f"{lhs}={eval(rhs)}")
        continue
    if rhs.isidentifier():
        copies[lhs] = copies.get(rhs,rhs)
        continue
    new_rhs = re.sub(r"\b(\w+)\b", lambda m: copies.get(m.group(1), m.group(1)), rhs)
    for expression, value in expressions.items():
        if expression in new_rhs:
            new_rhs = new_rhs.replace(expression, value)
    expressions[new_rhs] = lhs
    print(f"{lhs}={new_rhs}")