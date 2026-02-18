


presedence = {
    "¬": 5,
    "∧": 4,
    "∨": 3,
    "→": 2,
    "↔": 1
}

def shuntingYard(input : str):
    '''Shunting Yard or Dijkstras Algorithm'''

    # Limpiamos el input para dejar solo operadores y letras
    clean_input = list(input.strip().replace(" ",""))

    # Asignamos el output y el opstack(operator stack)
    output = []
    stack = []

    for token in clean_input:
        if token in presedence:

            # Mientras todavia tengamos elementos dentro del stack...
            while len(stack) > 0:
                '''En este while declaramos una variable [op] que se iguala al ultimo elemento
                del STACK, y luego comparamos su jerarquia con la del token actual. 
                Si el token actual es de mayor presedencia significa que se puede meter en el 
                STACK entonces rompemos ciclo, si no es el caso sacamos el operador del STACK 
                y lo metemos al OUTPUT, y seguimos comparando con el siguiente operador del 
                STACK'''

                op = stack[-1]

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

    return output
    
def applyBooleanValues(postfix):

    propositions = {
       'p': True,
       'q': False,
       'r': True,
    }
    
    #boolean reverse polish notation
    boolean_rpe = []
    for element in postfix:
        if element in propositions:
            boolean_rpe.append(propositions[element])
        else:
            boolean_rpe.append(element)

    return boolean_rpe


    pass

def performCalculation(output):
    result = []
    for element in output:
        if element not in presedence:
            result.append(element)
        else:
            right = result.pop()
            left = result.pop()

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
                


input = "p ↔ ¬q ∧ r"
shunt = shuntingYard(input)
print(shunt)
boolShunt = applyBooleanValues(shunt)
print(boolShunt)


