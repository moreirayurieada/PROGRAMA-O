dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digitee o divisor: "))

while dividendo >= divisor:
    dividendo -= divisor

print(f"O resto da divisão é: {dividendo}")
