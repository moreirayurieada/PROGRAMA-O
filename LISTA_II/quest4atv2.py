numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Escolha uma operação (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")
elif operacao == '-':
    resultado = numero1 - numero2
    print(f"Resultado da subtração: {resultado}")
elif operacao == '*':
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == '/':
    if numero2 == 0:
        print("Erro! Não é possível dividir por zero.")
    else:
        resultado = numero1 / numero2
        print(f"Resultado da divisão: {resultado}")
else:
    print("Operação inválida. Por favor, escolha +, -, *, ou /.")
