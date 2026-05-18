# Função de soma
def soma(a, b):
    resultado = a + b
    print("Resultado da soma:", resultado)

# Função de subtração
def subtracao(a, b):
    resultado = a - b
    print("Resultado da subtração:", resultado)

# Função de multiplicação
def multiplicacao(a, b):
    resultado = a * b
    print("Resultado da multiplicação:", resultado)

# Função de divisão
def divisao(a, b):
    if b != 0:
        resultado = a / b
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: divisão por zero!")

# Função principal
def main():
    print("CALCULADORA")

    operador = input("Digite a operação (+, -, x, /): ")

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if operador == "+":
        soma(valor1, valor2)

    elif operador == "-":
        subtracao(valor1, valor2)

    elif operador == "x":
        multiplicacao(valor1, valor2)

    elif operador == "/":
        divisao(valor1, valor2)

    else:
        print("Operação inválida!")

# Chamada da função principal
main()