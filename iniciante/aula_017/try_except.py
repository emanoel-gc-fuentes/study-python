# TEMA: try except

# try => Tentar executar um trecho de código
# except => Ocorreu algum erro ao tentar executar

# Ex. de excessão:
# print(123)
# int('a')

numero_str = input('Digite um número:')

try: # Tentar executar um trecho de código
    numero_int = int(numero_str)
    print(f'Este número ao quadrado é {numero_int ** 2 }')
except: # Ocorreu algum erro ao tentar executar
    print('Valor informado não é número')

