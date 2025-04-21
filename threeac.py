
def convert_to_threeac(expression):
    expression = expression.replace(" ","").replace(";","")

    lhs,rhs = expression.split("=")
    tem_count =1
    result = []

    while "(" in rhs:
        op_index = rhs.find("(")
        cl_index = op_index +1
        count = 1
        while count > 0:
            if rhs[cl_index] == "(":
                count +=1
            if rhs[cl_index] ==")":
                count-=1
            cl_index+=1
        cl_index-=1

        sub_exp = rhs[op_index+1:cl_index]

        if "+" in sub_exp:
            a,b = sub_exp.split("+")
            result.append(f"t{tem_count} = {a} + {b}")
        elif "-" in sub_exp:
            a,b = sub_exp.split("-")
            result.append(f"t{tem_count} = {a} - {b}")
        elif "*" in sub_exp:
            a,b = sub_exp.split("*")
            result.append(f"t{tem_count} = {a} * {b}")
        elif "/" in sub_exp:
            a,b = sub_exp.split("/")
            result.append(f"t{tem_count} = {a} / {b}")
        
        rhs = rhs[:op_index] + f"t{tem_count}" + rhs[cl_index+1:]
        tem_count+=1
    
    if "+" in rhs:
            a,b = rhs.split("+")
            result.append(f"t{tem_count} = {a} + {b}")
    elif "-" in rhs:
            a,b = rhs.split("-")
            result.append(f"t{tem_count} = {a} - {b}")
    elif "*" in rhs:
            a,b = rhs.split("*")
            result.append(f"t{tem_count} = {a} * {b}")
    elif "/" in rhs:
            a,b = rhs.split("/")
            result.append(f"t{tem_count} = {a} / {b}")
    else :
          result.append(f"t{lhs} = {tem_count}")
    
    result.append(f"{lhs} = t{tem_count}")

    return result










expression = "x = (a+b) * (c-d);"
threeac = convert_to_threeac(expression)
for lines in threeac:
     print(lines)