# OBJETIVO: Com os dados setados nas variáveis, hardcode, o código identificará o IMC (Indice de massa corporal);

nome = 'Emanoel'
idade = 24
altura = 1.70
peso = 90.0
imc = peso/(altura**2)


print('#'*16)
print('DADOS DO CLIENTE')
print('#'*16)
print(
    f'NOME: {nome}',
    f'IDADE: {idade}',
    f'ALTURA: {altura}',
    f'PESO: {peso}',
    f'IMC: {imc}',
    sep='\n'
)
print('#'*16)
