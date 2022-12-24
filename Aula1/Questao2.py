print("Use o sistema de 24h")
horaI = int(input("Insira as horas iniciais "))
minI  = int(input("Insira os minutos iniciais "))
horaF = int(input("Insira as horas finais "))
minF = int(input("Insira os minutos finais "))

res=((horaF * 60) + minF) - ((horaI * 60) + minI)

if(res <= 0):
  res+=24*60
    
hora=res//60
minuto=res%60
print("O JOGO DUROU", hora, "HORA(S)", "E", minuto, "MINUTO(S)")