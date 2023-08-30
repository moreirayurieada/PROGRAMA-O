salário = float(input("Digite o salário atual:"))
porcetagem = float(input("Digite a porcentagem de aumento:"))
aumento = salário * porcetagem / 100
novo_salário = salário + aumento
print("Um aumento de {} %% em um salário de R$ {}".format(porcetagem, salário))
print("é igual a um aumento de R$ {}".format(aumento))
print("Resultando em um novo salário de R$ {}".format(novo_salário))

