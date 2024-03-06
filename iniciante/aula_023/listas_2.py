#  append, insert, pop, del, clea, extend, 
# create, read, update, delete = CRUD
# criar,  ler,  alterar, apagar
from re import L


l_num = [10,20,30,40,50]
print(l_num)
# Atribuindo elemento há uma variável:
number_element = l_num[2] # 30

# del: deleta o elemento especificado pelo indice
del l_num[0]
print(f'del {l_num}')

# append: adiciona um novo elemento no último indice da lista
l_num.append(60)
print(f'append {l_num}')

# pop: Remove último elemento da lista
l_num.pop()
print(f'pop {l_num}')

# OBS: você consegue atrelar o valor removido há uma variável:
num_removed = l_num.pop()
print(f'lista: {l_num}, Valor Removido: {num_removed}')


# clear: Limpar lista:
l_num2 = l_num
print(l_num2)
l_num2.clear()
print(f'clear {l_num2}')


# insert: Adiciona um novo elemento em um index expecífico;
# inset(posição, elemento)
l_num = [10,20,30,40,50]
l_num.insert(2,0)
print(f'insert {l_num}')


# concatena:
nome = ['Emanoel']
sobrenome = ['Galdino']
nome_completo = nome + sobrenome
print(nome_completo)


# extend: quase como concatenar mas a lista onde o método foi aplicado que recebe os valores:

nome.extend(sobrenome)
print(f'extend {nome}')


# Observação: 
"""
CUIDADO AO SE UTILIZAR DADOS MUTAVEIS:

IMUTÁVEIS = copiado o valor
MUTÁVEIS = aponta para o mesmo valor na memória

"""

# Ex.:

# Imutável

# Mutável
l_numbers = [1,2,3,4,5,6]
l_numbers2 = l_numbers

# # Ao limpar a lista 2 a lista original será impactada: 
l_numbers2.clear()

print(f'Lista 01: {l_numbers}')
print(f'Lista 02: {l_numbers2}')

# Resolva essa situação utilizando o método copy:
l_numbersX = [1,2,3,4,5,6]
l_numbers3 = l_numbersX.copy()
l_numbers3.clear()

print(f'Lista X: {l_numbersX}')
print(f'Lista 03: {l_numbers3}')

