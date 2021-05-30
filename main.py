import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#Matplotlib wersja 1

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

#Matplotlib wersja 2

#Zadanie 1

# fig = plt.figure()
# ax = fig.gca(projection = '3d')
# z = np.linspace(0, 2 * np.pi, 100)
# t = z
# x = np.sin(z)
# y = 2 * np.cos(z)
# ax.plot(x, y, t, label='zadanie1')
# ax.legend()
# plt.show()

#Zadanie 2

# np.random.seed(19680801)
# def rand(n, vmin,vmax):
#     return (vmax - vmin) * np.random.rand(n) + vmin
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 2
#
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = rand(n, 23, 32)
#     ys = rand(n, 0, 100)
#     zs = rand(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('x label')
# ax.set_ylabel('y label')
# ax.set_zlabel('z label')
# plt.show()

#Zadanie 3

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# x = np.arange(-5, 5, 0.25)
# y = np.arange(-5, 5, 0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2 + y**2)
# z = np.sin(r)
# surf = ax.plot_surface(x, y, z, cmap=cm.BuPu, linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

#Zadanie 4
#dokonczyc

# fig = plt.figure(figsize=(8, 3))
# ax1 = fig.add_subplot(121, projection='3d')
# ax2 = fig.add_subplot(122, projection='3d')
# _x = np.arange(10)
# _y = np.arange(2)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Wykres nie zacieniony')
# plt.show()


#Zadanie 5

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# x = np.arange(-5, 5, 0.25)
# y = np.arange(-5, 5, 0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2 + y**2)
# z = np.sin(r)
# surf = ax.plot_surface(x, y, z, cmap=cm.BuPu, linewidth=0, antialiased=True)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()