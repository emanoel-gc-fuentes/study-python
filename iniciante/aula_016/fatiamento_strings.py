# TEMA: Fatiamento de Strings

#-7-6-5-4-3-2-1 => INDICE NEGATIVO
# P A L A V R A
# 0 1 2 3 4 5 6 => INDICE POSITIVO

# O fatiamento consiste em pegar um intervalo setado do texto
# OBSERVAÇÃO: Função len() => Retorna o total de caracteres de um str;

variavel = 'palavra'

# Pegando por indece
print(variavel[-4])
print(variavel[-2])

# fatiamento: [inicio:fim:passo(pular)]
print(variavel[3:])

print(variavel[:3])

print(variavel[1:4])

print(variavel[::-1])

print(len(variavel))

