def generate_precedence():
    return {
        '+':{'+':'>','*':'<','id':'<','$':'>'},
        '*':{'+':'>','*':'>','id':'<','$':'>'},
        'id':{'+':'>','*':'>','id':'-','$':'>'},
        '$':{'+':'<','*':'<','id':'<','$':'ACCEPT'}
    }



def display_table():
    table = generate_precedence()
    print("The Precedence Table ")
    print("   |  +   |  *  |  id |  $  ")
    for row in ['+','*','id','$']:
        print(f"{row:<2} |  {table[row].get('+',''):<2}  |  {table[row].get('*',''):<2} |  {table[row].get('id',''):<2} |  {table[row].get('$',''):<2}")

def precedence_parser(expression):
    operators = ['+','*','id','$']
    
    table = generate_precedence()
    tokens = []
    i=0
    while i < len(expression):
        if expression[i:i+2] == "id":
            tokens.append('id')
            i+=2
        else:
            tokens.append(expression[i])
            i+=1
        
    tokens.append('$')
    stack = ['$']
    i = 0
    print("The Parsing Table is : ")
    print("STACK\t\tINPUT\t\tACTION\n")

    while True:
        stack_top = next((s for s in reversed(stack) if s in operators),None)
        current_token = tokens[i]

        stack_str = ' '.join(stack)
        input_str = ' '.join(tokens[i:])

        if stack_top == "$" and current_token == "$":
            print(f"{stack_str:<30} | {input_str:<20} | ACCEPT")
        
        relation = table.get(stack_top,{}).get(current_token,None)

        if relation == '<':
            print(f"{stack_str:<30} | {input_str:<20} | Shift -> {current_token}")
            stack.append(current_token)
            i +=1
        
        elif relation == '>':
            if len(stack) >= 2 and stack[-1] == 'id':
                stack[-1] = 'E'
                print(f"{stack_str:<30} | {input_str:<20} | REDUCE : E -> id")
            elif len(stack) >= 3 and stack[-2] in ['+','*'] and stack[-1] == 'E' and stack[-3] =='E':
                operator = stack[-2]
                stack[-3:]=['E']
                print(f"{stack_str:<30} | {input_str:<20} | REDUCE : E {operator} E -> id")
    
        else : 
                return False
    






# terminal + , * id $
expression = "id+id*id"
display_table()
precedence_parser(expression)
