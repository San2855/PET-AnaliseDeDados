def valorPagamento(valor, dias):
    taxa = 0
    if dias == 0:
      return valor
    else:
      taxa = 0.01 * dias
      return valor + ((3/100 * valor)) + (taxa*valor) 
Valortotal = 0
cont = 0
valor = float(input('Digite o valor da prestação: '))
while valor > 0:
    dias = int(input('Digite o número de dias em atraso: '))
    Valorpagar = valorPagamento(valor, dias)
    Valortotal += Valorpagar
    cont += 1
    valor = float(input('Digite o valor da prestação: '))
    dias = int(input('Digite o número de dias em atraso: '))


print('Quantidade total de prestações: ', cont)
print('Valor total das prestações: ', Valortotal)