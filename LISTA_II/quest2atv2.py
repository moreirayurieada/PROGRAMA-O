salario_atual = float(input("Digite o valor do salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

aumento = (porcentagem_aumento / 100) * salario_atual
novo_salario = salario_atual + aumento

print(f"O valor do aumento é: R${aumento:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")
