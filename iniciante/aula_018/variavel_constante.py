# CONSTANTE: "Variáveis" que não mudam
# Ex.: Colunas de uma planilha: USUARIO = [NOME, IDADE, SEXO, RAZAO_SOCIAL] Lista de informações que serão a mesma coisa para qualquer novo registro.

# De acordo com as boas praticas da programação, é ruim utilizar muitas condições na mesma condicional, para corrigir

# Portanto, para contornar esse cenário, você pode atribuir a condicional a uma variável que condiz com a condicional.

VEL_PERMITIDA = 100
vel_atual = input('velocidade atual:')
int_vel_atual = int(vel_atual)
velocidade_aceita = int_vel_atual < VEL_PERMITIDA and int_vel_atual >= 0 or int_vel_atual ==  VEL_PERMITIDA

if velocidade_aceita:
    print('Dentro do limite permitido')
else:
    print('Fora do limite de velocidade estabelecido')
    print('MUTADO!')