string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

caracteres_comuns = ""

for caractere in string1:
    # Verificar se o caractere está na segunda string e não está na string resultante
    if caractere in string2 and caractere not in caracteres_comuns:
        caracteres_comuns += caractere

if caracteres_comuns:
    print("Caracteres comuns encontrados:", caracteres_comuns)
else:
    print("Não há caracteres comuns nas duas strings.")
