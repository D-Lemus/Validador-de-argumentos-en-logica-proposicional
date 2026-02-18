
presedence = {
    "¬": 5,
    "∧": 4,
    "∨": 3,
    "→": 2,
    "↔": 1
}

def _cleanInput(input:str):
    '''Function meant for elimminating blank spaces and segmenting each element of the string'''
    clean_input = list(input.strip().replace(" ",""))

    #Debugging purposes
    print(f'clean input:{clean_input}')
    print(80*'=')
    return clean_input

def shuntingYard(input : str):
    '''Shunting Yard algorythm that converts an arithmetic notation into a Reverse Polish Notation(RPN)'''
    clean_input = _cleanInput(input)

    # Asigning the output and stack as empty lists
    output = []
    stack = []

    for token in clean_input:
        
        #if 'token' is a left parenthesis, we will push it to the stack
        if token == '(':
            stack.append(token)

        #if 'token' is a right parenthesis, we will pop the operators from the stack to the output until we find a left parenthesis. We will discard the left parenthesis
        elif token == ')':
            while len(stack)>0:
                op = stack.pop()
                if op == '(':
                    break
                output.append(op)

        #If 'token' is an operator, we will check the presedence and associativity of the operators in the stack and move them to the output if necessary
        else:
            if token in presedence:
                # While there is an operator at the top of the stack with greater precedence, we will pop it to the output
                while len(stack) > 0:
                    op = stack[-1]
                    if op == '(':
                        break
                    if presedence[token]> presedence[op]:
                        break
                    stack.pop()
                    output.append(op)
                stack.append(token)
            else:
                output.append(token)

    #Sacar los operadores restantes del STACK al OUTPUT
    while len(stack) > 0:
        output.append(stack.pop())

    # Debugging purposes
    print(f"Reverse Polish Notation (RPE): {output}")
    print(80*'=')
    return output
    
def applyBooleanValues(postfix):
    '''Asigning a boolean value to each proposition in the RPN'''

    propositions = {
       'p': True,
       'q': False,
       'r': True,
       't' : False,
    }
    
    #boolean reverse polish notation
    boolean_rpe = []
    for element in postfix:
        if element in propositions:
            boolean_rpe.append(propositions[element])
        else:
            boolean_rpe.append(element)

    # Debugging purposes
    print(f"Boolean Values Replaced: {boolean_rpe}")
    print(80*'=')
    return boolean_rpe

def performCalculation(output):
    '''Performing calculations for unary and binary operators in the RPN'''
    result = []
    for element in output:
        if element not in presedence:
            result.append(element)
        else:
            right = result.pop()
            left = result.pop()

            # unary operator, so we only need the right operand
            if element == '¬':
                result.append(left)
                result.append(not right)
            elif element == '∧':
                result.append(left and right)
            elif element == '∨':
                result.append(left or right)
            elif element == '→':
                '''Equivalencia logica de p→q es ¬p∨q'''
                result.append(not left or right)
            elif element == '↔':
                '''Equivalencia logica de p↔q es (¬p∨q)∧(¬q∨p)'''
                result.append((not left or right)and(not right or left))

    #Debugging purposes
    print(f'result: {result}')
    
    return result


input = "(p∨q)∧(¬r→s)"
print(f"Input: {input}")
shunt = shuntingYard(input)
boolShunt = applyBooleanValues(shunt)
result = performCalculation(boolShunt)



