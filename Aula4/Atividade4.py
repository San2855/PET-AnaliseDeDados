import pandas as pd
from scipy import stats

data2022 = pd.read_csv('licitacoes-2022.csv', sep=',',
                       on_bad_lines='skip', low_memory=False)

data2021 = pd.read_csv('licitacoes-2021.csv', sep=',',
                       on_bad_lines='skip', low_memory=False)


data2022.dropna(subset=['VALORESTIMADO'], inplace=True)
data2021.dropna(subset=['VALORESTIMADO'], inplace=True)

media2022 = data2022['VALORESTIMADO'].mean()
media2021 = data2021['VALORESTIMADO'].mean()

minimo2022 = data2022['VALORESTIMADO'].min()
minimo2021 = data2021['VALORESTIMADO'].min()

maximo2022 = data2022['VALORESTIMADO'].max()
maximo2021 = data2021['VALORESTIMADO'].max()

desvio2022 = data2022['VALORESTIMADO'].std()
desvio2021 = data2021['VALORESTIMADO'].std()

variancia2022 = data2022['VALORESTIMADO'].var()
variancia2021 = data2021['VALORESTIMADO'].var()

print("____________MÉDIA DAS LICITAÇÕES____________")
print("A média de licitações no ano de 2022 foi de:", media2022)
print("A média de licitações no ano de 2021 foi de:", media2021)
print("__"*30)

print("____________MENORES VALORES DA LICITAÇÕES____________")
print("O menor valor de uma licitação no ano de 2022 foi de:", minimo2022)
print("O menor valor de uma licitação no ano de 2021 foi de:", minimo2021)
print("__"*30)

print("____________MAIORES VALORES DA LICITAÇÕES____________")
print("O maior valor de uma licitação no ano de 2022 foi de:", maximo2022)
print("O maior valor de uma licitação no ano de 2021 foi de:", maximo2021)
print("__"*30)

print("____________DESVIO PADRÃO DAS LICITAÇÕES____________")
print("O desvio padrão das licitações no ano de 2022 foi de:", desvio2022)
print("O desvio padrão das licitações no ano de 2021 foi de:", desvio2021)
print("__"*30)

print("____________VARIÂNCIA DAS LICITAÇÕES____________")
print("A variância das licitações no ano de 2022 foi de:", variancia2022)
print("A variância das licitações no ano de 2021 foi de:", variancia2021)
print("__"*30)

t_stat, p_value = stats.ttest_ind(
    data2022['VALORESTIMADO'], data2021['VALORESTIMADO'], equal_var=False)

# # Print results
print("Resultado do t-statistic:", t_stat)
print("p-value:", p_value)


#____________MÉDIA DAS LICITAÇÕES____________
#A média de licitações no ano de 2022 foi de: 1054520.0687931033
#A média de licitações no ano de 2021 foi de: 890532.0154205608
#Aqui vemos que a média de valores em 2022 foi maior que em 2021.
#____________________________________________________________
#____________MENORES VALORES DA LICITAÇÕES____________
#O menor valor de uma licitação no ano de 2022 foi de: 0.0
#O menor valor de uma licitação no ano de 2021 foi de: 59.0
#Aqui vemos que o ano de 2022 teve a licitação mínima mais barata que em 2021.       
#____________________________________________________________
#____________MAIORES VALORES DA LICITAÇÕES____________
#O maior valor de uma licitação no ano de 2022 foi de: 11200034.32       
#O maior valor de uma licitação no ano de 2021 foi de: 10786389.69
#Aqui vemos que o ano de 2022 teve a licitação máxima mais cara que em 2021.       
#____________________________________________________________
#____________DESVIO PADRÃO DAS LICITAÇÕES____________
#O desvio padrão das licitações no ano de 2022 foi de: 1800922.4912754374
#O desvio padrão das licitações no ano de 2021 foi de: 1613621.1855932986
#Isso indica que a dispersão dos valores das licitações foi similar em ambos os anos.
#____________________________________________________________
#____________VARIÂNCIA DAS LICITAÇÕES____________
#A variância das licitações no ano de 2022 foi de: 3243321819581.728
#A variância das licitações no ano de 2021 foi de: 2603773330595.5225
#Isso indica que a variabilidade dos valores das licitações foi maior em 2022 do que em 2021.
#____________________________________________________________
#Resultado do t-statistic: 0.7171108193762045
#p-value: 0.4740635623560422