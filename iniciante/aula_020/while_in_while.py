# While dentro de While

qnt_rows = 5
qnt_columns = 5

row = 1

while row <= qnt_rows:
    column = 1    
    while column <= qnt_columns:
        print(f'Linha: {row}, Coluna: {column}')
        column += 1
    
    row += 1

print('Acabou!')


