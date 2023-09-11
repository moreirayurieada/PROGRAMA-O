dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

resto = dividendo

while resto >= divisor:
    resto -= divisor

print(f"O resto da divisão de {dividendo} por {divisor} é {resto}")
