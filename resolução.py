# Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.

## Utilizando While

# numero = 0

# while numero <= 100:
#     print(numero)
#     numero += 1

## Utilizando For

# for num in range(0, 101):
#     print(num)

# Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.

# numero = 0
# n = int(input('Digite o último número da lista: '))

# while numero <= n:
#     print(numero)
#     numero += 1

## Utilizando For

# n = int(input('Digite o último número da lista: '))

# for num in range(0, n+1):
#     print(num)

# Faça um programa que diz se o número inserido é par ou ímpar.

# numero = int(input('Digite um inteiro: '))

# if numero == 0:
#     print(f"O número {numero} é neutro!")
# elif numero%2 == 0:
#     print(f"O número {numero} é par!")
# else:
#     print(f"O número {numero} é ímpar!")

# Faça um programa que imprima a quantidade de números pares entre dois números da sua escolha.

## Utilizando While

# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite outro número: '))
# i = 0

# while n1<=n2:
#     if (n1 % 2) == 0:
#         i = i + 1
#     n1 = n1 + 1
# print(i)

## Utilizando For

# inicio = int(input('Insira o Nº inicial: '))
# fim = int(input('Insira o Nº final: '))
# counter = 0

# for n in range(inicio, fim + 1):
#     if n % 2 == 0:
#         counter += 1

# print(f'Existem {counter} números pares entre {inicio} e {fim}.')

# Faça um programa que imprima a soma de todos os números pares entre dois números da sua escolha.

# lista = []
# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite outro número: '))
# i = 0

# while (n1<=n2):
#     if (n1 % 2) == 0:
#         lista.append(n1)
#     n1 = n1 + 1
    
# somalista = sum(lista)
# print(lista)
# print(f'A soma de números pares é: {somalista}')

## Usando For

# inicio = int(input('Insira o Nº inicial: '))
# fim = int(input('Insira o Nº final: '))
# soma = 0

# for n in range(inicio, fim + 1):
#     if n % 2 == 0:
#         soma += n

# print(f'A soma de todos os números pares entre {inicio} e {fim} é de {soma}.')

# Faça um programa que recebe um inteiro do usuário e diz se esse número é múltiplo de 3 ou não.

# numero = int(input('Digite um inteiro: '))

# if numero%3==0:
#     print(f"O número {numero} é múltiplo de 3")
# else:
#     print(f"O número {numero} não é múltiplo de 3")

## Usando not

# numero = int(input('Digite um inteiro: '))

# if not numero%3:
#     print(f"O número {numero} é múltiplo de 3")
# else:
#     print(f"O número {numero} não é múltiplo de 3")

# Faça um programa para sortear um número aleatório em uma lista de 1 ao 9.

# import random
# Lista = [1,2,3,4,5,6,7,8,9]
# index = random.randint(0, len(Lista) - 1)
# elemento = Lista[index]
# print(elemento)

# Faça um programa que mostre o fatorial de um número.

## Utilizando While

# n = int(input("Digite o valor de n: "))
# fat = 1
# i = 2

# while i <= n:
#     fat = fat*i
#     i = i + 1
# print(f"O valor de {n}! é = {fat}")

## Utilizando For