import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Zadanie 1
# x = np.arange(20, 41, 1)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.axis([20, 40, 0.02, 0.05])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('Wykres funkcji')
# plt.show()

#Zadanie 2
# x = np.arange(20, 41, 1)
# plt.plot(x, 1/x, 'bo--', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([20, 40, 0.02, 0.05])
# plt.legend()
# plt.title('Wykres funkcji')
# plt.show()

#Zadanie 3
# x = np.arange(0, 45, 0.1)
# plt.plot(x, np.sin(x), label='sin(x)')
# plt.plot(x, np.cos(x), label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend()
# plt.title('Wykres sin(x) i cos(x)')
# plt.show()

#Zadanie 4
# x = np.arange(0, 45, 0.1)
# plt.plot(x, np.sin(x) + 2, label='sin(x)')
# plt.plot(x, np.sin(x) * (-1), label='sin(x)')
# plt.xlabel('sin(x)')
# plt.ylabel('sin(x)')
# plt.legend(loc='center left')
# plt.title('Wykres sin(x) i sin(x)')
# plt.show()

#Zadanie 5

# df = pd.read_csv('iris.data', sep=';', decimal='.', header=None)
# # print(df)
# kolor = np.random.randint(0, 50, 50)
# Nie mam pojęcia jak zrobić

# plt.show()

#Zadanie 6
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# plt.subplot(1, 3, 1)
# urodzenia = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
# urodzenia.plot.bar(color=['y','b'])
# plt.xlabel('Płeć')
# plt.show()  #<--- nie wiem czy dobrze zrobione zadanie




# plt.subplot(1, 3, 2)
# a = df['Rok'].unique()
# kobiety = df[(df['Plec'] == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df['Plec'] == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(a, kobiety, label='kobiety')
# plt.plot(a, mezczyzni, label='mezczyzni')
# plt.ylabel('Liczba urodzonych dzieci')
# # plt.show()

# plt.subplot(1, 3, 3)
# b = df['Rok'].unique()
# c = df.groupby('Rok').agg({'Liczba': ['sum']}).values.flatten()
# plt.bar(b, c)
# plt.show()

#Zadanie 7
# df = pd.read_csv('zamowienia.csv', sep=';', decimal='.')
# suma = df.groupby('Sprzedawca')['Utarg'].sum()
# explode = [0.0 for n in range(len(suma.index))]
# explode[np.random.randint(0, len(suma.index))] = 0.2
# suma.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode, shadow=True)
# plt.title('Procentowy udział każdego sprzedawcy')
# plt.show()