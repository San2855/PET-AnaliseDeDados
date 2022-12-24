idade = 0
soma = 0
cont = 0
while idade >= 0:
  idade = int(input("Insira a idade do individuo "))
  if idade >= 0:
    cont += 1
    soma += idade
media = soma/cont

print(media)