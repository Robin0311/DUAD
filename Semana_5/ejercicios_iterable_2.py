# 2-Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

# 1. Pista: investigue de que otras maneras se puede usar el `range`.

name = 'Robinson Cerrato'

for i in range(len(name) - 1, -1, -1):
    print(name[i])
