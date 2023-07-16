"""# Implementar uma solução em Python que retornar a soma de todos os elementos pares de uma lista
def ehpar(n):
    r = n%2 == 0
    return r    

def soma_dos_pares(lista):
    soma =  0
    for elem in lista:
        if ehpar(elem):
            soma+= elem
    return soma        

lista_teste = [2,3,4,7,8,25,10]
resultado = soma_dos_pares(lista_teste)
print(f"A soma dos pares da lista é: {resultado}")"""


"""# Calcular o fatorial de um número
def calcular_fatorial(fatorial):
    f = 1
    for i in range(1,fatorial+1):
        f *= i
    return f


numero = eval(input("Calcule o fatorial de um número: \n"))
resultado = calcular_fatorial(numero)
print(f"O fatorial do número {numero} é : {resultado}")"""

# Determine se um número é ou não primo
def r_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n%i == 0:
            return False
        i-=1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f"O número {numero} não é primo!"
    if resultado:
        mensagem = f"O número {numero} é primo!"
    return mensagem


numero = eval(input("Digite um número: "))
resultado = r_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
