# TIPOS DE DADOS: STRING

# Strings são textos dentro de aspas: 

"Emanoel"
'Emanoel'

# o dado será considerado string estando dentro de aspas duplas ou aspas simples. 

# Em python, você consegue validar o tipo de dado através da funcação type()


print(
    type("Emanoel"),
    type('Emanoel'),
    sep="\n\n"
)

# Recomento que na programação você utilize as aspas simples, pois as aspas duplas são usadas com mais frequências em frases e textos.

### ESCAPE \: 

# Em casos onde você está usando aspas duplas e no meio do texto você possui um trecho que utiliza "" utilizar o escape para contonar a situação:

print("Eu sou \"Emanoel\" ")

### r
# Em casos onde você precisa que o \ apareça também, utilize 'r' antes de passar o atributo: 

print(r"Eu sou \"Emanoel\" ")

# Geralmente este r é utilizado para expressões regulares;