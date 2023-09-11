while True:
    # Exibir o menu de opções
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

escolha = input("Escolha uma opção (1/2/3/4/5): ")

if escolha == '1':
        numero = int(input("Digite um número para a tabuada de adição: "))
        for i in range(1, 11):
            resultado = numero + i
            print(f"{numero} + {i} = {resultado}")
        elif escolha == '2':
        numero = int(input("Digite um número para a tabuada de subtração: "))
        for i in range(1, 11):
            resultado = numero - i
            print(f"{numero} - {i} = {resultado}")
        elif escolha == '3':
        numero = int(input("Digite um número para a tabuada de multiplicação: "))
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        elif escolha == '4':
        numero = int(input("Digite um número para a tabuada de divisão: "))
        for i in range(1, 11):
            if i != 0:
                resultado = numero / i
                print(f"{numero} / {i} = {resultado}")
            else:
                print(f"Não é possível dividir por zero.")
        elif escolha == '5':
        print("Saindo do programa.")
        break
        else:
        print("Opção inválida. Escolha uma opção válida (1/2/3/4/5).")
