while True:
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = int(input("Escolhe a opcão! "))

    if escolha == 5:
        print("saindoooo")
        break

    num = int(input("digita um numero: "))

    for i in range(1, 11):
        if escolha == 1:
            resultado = num + i
            operacao = "+"
        elif escolha == 2:
            resultado = num - i
            operacao = "-"
        elif escolha == 3:
            resultado = num * i
            operacao = "x"
        elif escolha == 4:
            resultado = num / i
            operacao = "/"

            print(f"{num} {operacao} {i} = {resultado:.2f}")
            continue

        print(f"{num} {operacao} {i} = {resultado}")
