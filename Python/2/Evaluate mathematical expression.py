import re
def calc(expression):
    expression = expression.replace(" ","")
    # Si il y a 2 signes d'opération consécutifs, on retourne None
    if re.search(r"[\+\-\*\/]{2,}",expression):
        return None
    # Cherche un signe d'opération
    if re.search(r"[\+\-\*\/]",expression):
        # Retourne les signes d'opération
        operators = re.findall(r"[\+\-\*\/]",expression)
        # Récupère les valeurs avant et après le signe d'opération dans expression
        sum = 0
        for operator in operators:
            values = expression.split(operator)
            value1 = int(values[0][-1])
            value2 = int(values[1][0])
            # print(value1, operator, value2)
            print(value1, operator, value2)
            sum += calcul(value1, value2, operator)
            expression = replace(expression, value1, value2, operator)
        return sum
    
        

def calcul(value1, value2, operator):
    return value1 + value2 if operator == "+" else value1 - value2 if operator == "-" else value1 * value2 if operator == "*" else value1 / value2 if operator == "/" else None

# Fonction qui remplace value1, value2 et operator par le resultat de l'opération
def replace(expression, value1, value2, operator):
    return expression.replace(str(value1) + operator + str(value2), str(calcul(value1, value2, operator)))  

print(calc("1 + 1"))
print(calc("2 - 1"))
print(calc("2 * 3"))
print(calc("6 / 2 + 1"))