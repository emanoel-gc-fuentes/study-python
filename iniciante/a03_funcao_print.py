# FUNÇÃO PRINT(): Utilizada para imprimir argumentos no terminal. 
# ARGUMENTOS NÃO NOMEADOS: Dados passados dentro do parênteses sem expecificar o que são.

# Ex. - Imprimir o nome Emanoel G. Cardoso no terminal:
print("Emanoel G. Cardoso")

# Ex. - Imprimir a sequência numérica 1,2,3,4,5,6,7,8,9 no terminal:
print(1,2,3,4,5,6,7,8,9)

### ALTERAR O SEPARADOR:
# É possível alterar o separador padrão através do argumento nomeado "sep":

# Ex. - Altere o separado para "-"
print(999,999,999,99, sep="-")

# Ex. - Altere o separado para pular linhas:
print(999,888,777,666, sep="\n")

### ALTERAR O FINAL:
# É possível alterar o argumento nomeado "end" para mudar o do argumento do print

# Ex. - Adicionar Valor em Dollar:
print(2,501,sep=".", end=" R$")