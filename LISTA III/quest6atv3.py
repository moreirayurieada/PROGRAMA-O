def eh_palindromo(numero):
    return str(numero) == str(numero)[::-1]


numero =int(input("Digite um número: "))

if eh_palindromo(numero):
    print("{} é um número palíndromo." .format(numero))
else:
    print("{} não é um número palíndromo.".format(numero))
