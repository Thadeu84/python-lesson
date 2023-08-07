#Estruturas Lógicas, Condicionais e de Repetição em Python 

####
nome = input("Digite um nome:")

print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" %(nome))

print("Hello, World")
####

####
valor1 = 10
valor2 = 20

if valor1 > valor2:
    print ('O valor1 é maior do que o valor2')

else:
    print ('O valor2 é maior do que o valor1')
####

####
cor = "alguma cor"

if cor == 'verde' :
    print ('acelerar')

elif cor == 'amarelo' :
    print ('Atenção')

else:
    print ('Parar')
####

####
qtde_faltas = int(input("Digite a quantidades de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
####

####
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")
####

####
nome = "Guido"

for c in nome:
    print(c)

nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")
####

####
for x in range(5):
    print(x)
####

# Exemplo de uso do break
disciplina = "Linguagem de programção"

for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)
####

####
# Exemplo de uso do continue
disciplina = "Linguagem de programção"
for c  in disciplina:
    if c == 'a':
        continue
    else:
        print(c)
####

####
# Implementando Soluções em Python Mediante Funções
a = 2
b = 1

equacao = input("Digite aformuls geral da equação linear (a * x +b): ")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")