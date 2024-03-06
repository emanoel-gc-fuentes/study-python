# TEMA: Listas mutáveis em Python
# type: list / method: list()
# Suporta vários valores  de qualquer tipo;

# Métodos frequentemente utilizados: append(), insert(), pop(), del(), clear(), extend() ...

string = 'TEXTO'

# sintax: variável = []

l_data = [123, True, 'Emanoel', 1.5, ['teste', 'abc']] 
print(f'Lista | l_data: {l_data}')

# Acessando dado por indice - OBS.: Considerar que a contagem sempre começa em 0
print(f'Indice 2 | l_data[2]: {l_data[2]}') # Emanoel

print(f'{l_data[4][0].upper()}')

# Alterar valor de um elemento/indice:
l_data[1] = False
print(l_data)
