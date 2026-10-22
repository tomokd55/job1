def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "i":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    elif operator == "%":
        return num1%num2
    else:  
        return "Opérateur non valide"
print(calcule(10, "+", 5))
print(calcule(10, "-", 5))
print(calcule(10, "*", 5))
print(calcule(10, "/", 5))
print(calcule(10, "%", 5))
