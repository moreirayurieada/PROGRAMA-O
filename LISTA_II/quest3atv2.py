distancia_km = float(input("Digite a distância a percorrer (em quilômetros): "))
velocidade_media_kmph = float(input("Digite a velocidade média esperada (em km/h): "))

tempo_horas = distancia_km / velocidade_media_kmph

tempo_em_minutos = tempo_horas * 60
tempo_em_segundos = tempo_horas * 3600

print(f"Tempo da viagem: {int(tempo_horas)} horas, {int(tempo_em_minutos % 60)} minutos e {int(tempo_em_segundos % 60)} segundos")
