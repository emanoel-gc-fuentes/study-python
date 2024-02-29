# TEMA: Operadores Lógicos

# in (está entre)
# not in (não está entre)

# name = '' => Vazio
name = input('Seu nome:')

if name not in '':
    print(f'Nome computado: {name}')

if name in '':
    print('Nome não informado')


# OBSERVAÇÃO: Strings são iteráveis. A iteração é feita através dos indices;
