# Flag - Bandeira - Marcar um local
# None - Não valor
# is e is not - é ou não é (Tipo, Valor, Identidade)
# id = Identidade

# Não é uma boa prática declarar variáveis dentro de bloco de códigos, pois pode gerar erros no código no ato da interpretação:
status = False

if status:
    validator = True
else:
    ...
# A condicional acima não passa pelo bloco de código onde é declarado o validator assim, o interpretador não reconhece que foi definido esta variável.
    
# print(validator)
    

