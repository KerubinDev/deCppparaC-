num1 = float(input("Digite o primeiro numero: "))
operador = float(input("Digite o operador: "))
num2 = float(imput("Digite o segundo numero"))


if operador == '+':
    print(num1 + num2)
elif operador == '-':
    print(num1 - num2)
elif operador == '*':
    print(num1 * num2)
elif operador == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro >:(  não é possivel dividir por zero")
else:
    print("Operador invalido")