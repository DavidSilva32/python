# Tratamento de exceções na linguagem Python

# # Ecercício 01
# while True:
#     try:
#         int(input("Enter a number: \n"))
#         break
#     except ValueError:
#         print("Entre com um número válido!") 

# Exercício 02
def dividir(a,b):
    try:
        resposta = a/b
        print(f"A resposta é: {resposta}")
    except ZeroDivisionError:
        print("Divisão por zero")
    except TypeError:
        print("Digite um número")

dividir(5,6)