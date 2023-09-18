peso=float(input("Digite seu peso em KG: "))
altura=float(input("Digite sua altura em metros: "))
imc=peso/(altura*2)
print("Seu IMC é:{:.1f}".format(imc))
if imc <=18.5:
    print("Abaixo pesa")
elif 18.5 <= imc <25:
    print("Peso ideal")
elif 25 <= imc  <30:
    print("Acima do peso")
elif 30 <= imc < 40:
    print("Obesidade")
elif 40< imc :
    print("Obesidade 2")

