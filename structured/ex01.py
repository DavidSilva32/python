"""# Estruturas de Decisão - Exercício 01
numero = 3

if numero % 2 == 0:
    situacao = f"O número {numero} é par!"
else:
    situacao = f"O número {numero} é ímpar!"

print(situacao)"""

"""# Exercício 02
nota = 6

if nota >= 7:
    situacao = f"Estudante foi aprovado, pois sua nota é {nota}!"
elif nota >= 5:
    situacao = f"O estudante está em recuperação, pois usa nota é {nota}!"
else:
    situacao = f"O estudante foi reprovado, pois sua nota é {nota}!"

print(situacao)"""

"""# Exercício 03
unidade = eval(input("Quantas unidades do produto: "))
valor_unitario = 10
valor_da_compra = unidade * valor_unitario
desconto10 = 0.1
desconto20 = 0.2

if unidade >= 20:
    valor_com_desconto = valor_da_compra * (1 - desconto20)
    valor_final = (
        f"Ganhou desconto de 20%, valor da compra com desconto: R${valor_com_desconto}"
    )
elif unidade >= 11:
    valor_com_desconto = valor_da_compra * (1 - desconto10)
    valor_final = (
        f"Ganhou desconto de 10%, valor da compra com desconto: R${valor_com_desconto}"
    )
else:
    valor_final = f"Valor da compra atual é: R${valor_da_compra}"

print(valor_final)"""

# Exercício 04 - Implementar uma solução em Python, que some todos os números pares de uma lista.
lista = [10, 2, 5, 7, 6, 3]
soma = 0

for num in lista:
    if num % 2 == 0:
        soma += num

print(soma)