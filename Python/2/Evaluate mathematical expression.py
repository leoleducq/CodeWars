import re
def calc(expression):
    expression = expression.replace(" ","")
    # Si il y a 2 signes d'opération consécutifs, on retourne None
    if re.search(r"[\+\-\*\/]{2,}",expression):
        return None
    # Cherche un signe d'opération
    if re.search(r"[\*\/]",expression):
        sum, expression = determinate("*","/",expression,"(\d+(?:\.\d+)?)[\*\/](\d+(?:\.\d+)?)")
    if re.search(r"[\+\-]",expression):
        sum, expression = determinate("+","-",expression, "(\d+(?:\.\d+)?)[\+\-](\d+(?:\.\d+)?)")
    try:
        return sum
    except:
        return re.search(r"(\d+(?:\.\d+)?)",expression).group()

def determinate(sign1,sign2, expression,regex_calcul):
    while sign1 in expression or sign2 in expression:
        calculs = re.search(rf"{regex_calcul}",expression).group()
        # Récupère les valeurs avant et après le signe d'opération
        values = re.findall(r"(\d+(?:\.\d+)?)",calculs)
        # Récupère le signe d'opération
        operator = re.search(r"[\+\-\*\/]",calculs).group()
        # Fait le calcul
        sum = calcul(values[0],values[1],operator)
        # Remplace value1, value2 et operator par le resultat de l'opération
        expression = replace(expression, values[0], values[1], operator)
    return sum,expression

def calcul(value1, value2, operator):
    # Change les valeurs en float
    value1 = float(value1)
    value2 = float(value2)
    return value1 + value2 if operator == "+" else value1 - value2 if operator == "-" else value1 * value2 if operator == "*" else value1 / value2 if operator == "/" else None

# Fonction qui remplace value1, value2 et operator par le resultat de l'opération
def replace(expression, value1, value2, operator):
    return expression.replace(str(value1) + operator + str(value2), str(calcul(value1, value2, operator)))

print(calc("10- 2- -5"))
print(calc("(((10)))"))
print(calc("1 -- 1"))
print(calc("1 + 1"))
print(calc("2 - 1"))
print(calc("2 * 3"))
print(calc("2 / 2"))
print(calc("6 / 2 + 1 * 4 / 2"))