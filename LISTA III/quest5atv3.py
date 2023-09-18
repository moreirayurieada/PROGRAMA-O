casa=int(input("Digite o valor da casa pretendida: "))
salario=int(input("Digite o valor do seu salario em reais (R$): "))
anos=int(input("Digite em quantos  anos você quer pagar a casa: "))

anos=anos*12
prestacao=casa/anos
psalario=salario*0.30

if prestacao > psalario:
    print("EMPRESTIMO NEGADO")
elif prestacao <= psalario:
    print("EMPRESTIMO ACEITO")
    print("O valor das parcelas ficaram em: R${}".format(prestacao))


