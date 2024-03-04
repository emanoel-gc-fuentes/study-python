# OBJETIVO: Criar um sistema para registro de usuários:
# 
# NOME COMPLETO
# IDADE
# DATA DE NASCIMENTO
# E-MAIL
# PROFISSÃO
# SEXO
# SALÁRIO
import datetime
import os
from time import sleep

def header():
    print('#'*40, '           CADASTRO DE USUÁRIO', '#'*40, sep='\n')

status = True

while status:

    header()
    nome_completo = input('NOME COMPLETO: ')
    if ' ' not in nome_completo:
        print('INFORME SEU NOME COMPLETO')
        sleep(0.5)
        os.system('cls')
        continue
    else: 
        os.system('cls')
        print('COMPUTADO COM SUCESSO')
        sleep(0.5)
        os.system('cls')

    header()
    data_nascimento = input('DATA DE NASCIMENTO (DD/MM/AAAA): ')
    if '/' not in data_nascimento:
        print('INFORME SUA DATA DE NASCIMENTO CONFORME ORIENTADO (DD/MM/AAAA)')
        sleep(0.5)
        os.system('cls')
        continue
    else: 
        os.system('cls')
        print('COMPUTADO COM SUCESSO')
        sleep(0.5)
        os.system('cls')

    header()
    idade = input('IDADE: ').isdigit()

    sexo = ...
    email = ...
    profissao = ...
    salario = ...






    status = False