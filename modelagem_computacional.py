## Modelagem computacional##
## Vacinação ##

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

fig, ax = plt.subplots()

pessoas=int(input('quantas pessoas? ')) #numero de pessoas

placebo=int(input('quantas pessoas recebram placebo? (placebo deve ser maior que o numero de vacinado) ')) # pessoas que receberam o placebo

vacina=int(input('quantas pesssoas receberam vacina? '))  #pessoas que receberam a vacina

a = vacina/placebo #divide o numero de vacinados pelo numero de pessoas que não receberam vacina

b = 1 - a # faz a diferença do total(1) na divisão da vacina pelo placebo, encontrando o percentual em decimal

em = b * 100 # multiplica por 100 para tirar os decimais

ax.scatter([em], [em], label='Porcentagem de Eficácia')


x = np.arange(0.5, pessoas, 10)

ax.plot(x, x, label='pessoas')  # monta a funçao linear

ax.set_title('vacina'); #titulo
ax.legend()

plt.xlabel('percentual') #Define um nome para o eixo "x"

plt.ylabel('percentual') #Define um nome para o eixo "y"

print('a eficácia é de {:.2f}%' .format(em)) #mostra a porcentagem

plt.grid(True) #colocar grid


plt.show() #mostrar