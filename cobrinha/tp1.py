import re

def calcular_expressao():
    expressao = input("Digite uma expressão matemática (exemplo: 2 * 2): ")
    expressao = expressao.replace(" ", "")
    
    if re.match(r'^[0-9+\-*/]+$', expressao):
        resultado = eval(expressao)
        print(f"O resultado da expressão é: {resultado}")
    else:
        print("Erro: A expressão contém caracteres inválidos.")

calcular_expressao()