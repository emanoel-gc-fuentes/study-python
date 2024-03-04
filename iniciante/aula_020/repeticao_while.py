# TEMA: Repetições "Enquanto" 
"""
Sintax:

while condição:
    bloco de código, enquanto a condição for verdadeira;
"""

contador = 0

# while contador < 10:
#     print(contador)
#     contador = contador + 1
#     print(f'adicionado 1 ao contador', f'Valor atual: {contador}')

# print('Loop while encerrado!')

####################################

#2) Adicionando "continue" que quando usado, ignora o código abaixo e reinicia o loop:

while contador < 100:
    contador += 1 
    
    if contador == 49:
        print('49 Removido')
        continue
    
    if contador == 50:
        print(contador)
        break

    print(contador)
    
print('Acabou')
