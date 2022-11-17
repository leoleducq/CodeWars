import re
def calc(expression):
    expression = expression.replace(" ","")
    # Si il y a 2 signes d'opération consécutifs, on retourne None
    if re.search(r"[\+\-\*\/]{2,}",expression):
        return None
    # Cherche un signe d'opération
    if re.search(r"[\+\-\*\/]",expression):
        while "*" in expression or "/" in expression:
            calculs = re.search(r"(\d+(?:\.\d+)?)[\*\/](\d+(?:\.\d+)?)",expression)
            # Récupère les valeurs avant et après le signe d'opération
            values = re.findall(r"(\d+(?:\.\d+)?)",calculs.group())
            # Récupère le signe d'opération
            operator = re.search(r"[\+\-\*\/]",calculs.group()).group()
            # Fait le calcul
            sum = calcul(values[0],values[1],operator)
            # Remplace value1, value2 et operator par le resultat de l'opération
            print("{} : {} {} {} = {}".format(expression, values[0],operator,values[1],sum))
            expression = replace(expression, values[0], values[1], operator)

        while "+" in expression or "-" in expression:
            calculs = re.search(r"(\d+(?:\.\d+)?)[\+\-](\d+(?:\.\d+)?)",expression)
            values = re.findall(r"(\d+(?:\.\d+)?)",calculs.group())
            operator = re.search(r"[\+\-\*\/]",calculs.group()).group()
            sum = calcul(values[0],values[1],operator)
            print("{} : {} {} {} = {}".format(expression,values[0],operator,values[1],sum))
            expression = replace(expression, values[0], values[1], operator)
        return sum

def calcul(value1, value2, operator):
    # Change les valeurs en float
    value1 = float(value1)
    value2 = float(value2)
    return value1 + value2 if operator == "+" else value1 - value2 if operator == "-" else value1 * value2 if operator == "*" else value1 / value2 if operator == "/" else None

# Fonction qui remplace value1, value2 et operator par le resultat de l'opération
def replace(expression, value1, value2, operator):
    return expression.replace(str(value1) + operator + str(value2), str(calcul(value1, value2, operator)))  

calc("1 + 1")
calc("2 - 1")
calc("2 * 3")
calc("2 / 2")
calc("6 / 2 + 1 * 4 / 2")