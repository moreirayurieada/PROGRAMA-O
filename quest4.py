
print("BEM VINDE A CALCULADORA kkkkkk")
n1=float(input("Digite um numero: "))
n2=float(input("Digite mais um numero: "))
operação=input("Qual ação deseja realizar?  +  -  *  /  ")
if operação == "+":
    resultado = n1 + n2
elif operação == "-":
    resultado = n1 - n2
elif operação == "*":
    resultado = n1 * n2
elif operação == "/":
    resultado = n1 / n2
else:
    print("INVALIDO!")
    resultado=0
print("Resultado da operação: {}".format(resultado))
