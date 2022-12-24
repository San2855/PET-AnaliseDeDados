def CalculaSalario():
  salario = int(input("Digite seu Salario: "))
  IR = 15/100
  INSS = 11/100
  S_INSS = salario - (salario * INSS)
  salarioLiquido = S_INSS - (S_INSS * IR)
  print(salarioLiquido)

CalculaSalario()
