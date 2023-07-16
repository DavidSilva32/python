# Programação Concorrente - Exemplo
# from threading import Thread
# from time import sleep, time


# def tarefa(tempo_espera, mensagem):
#     print(f"Iniciando a tarefa! {mensagem}")
#     sleep(tempo_espera)
#     print(f"Conclusão da tarefa! {mensagem}")


# thread = Thread(target=tarefa, args=(2, "Thread em execução"))
# thread.start()
# print("Aguardando pela execução da thread...\n")
# thread.join()
# print("Concluída a execução!")

# # Exercício 01
# from threading import Thread
# from time import sleep


# def tarefa(time, task_name):
#     print(f"Iniciando a tarefa {task_name}")
#     sleep(time)
#     print(f"Conclução da terfa {task_name}")

# lista_t = [] # Criação de uma lista para threads
# lista_t.append(thread1 = Thread(target=tarefa, args=(3, "A"))) #acrescentando uma thread a lista
# lista_t.append(thread1 = Thread(target=tarefa, args=(3, "A"))) #acrescentando uma thread a lista
# for thread in lista_t: # Iniciando as threads
#     thread.start()
# print("Aguardando pela execução das threads...")
# for thread in lista_t: # esperar a execução de cada thread
#     thread.join()
# print("A execução foi concluída!")

# Exercício 02
from threading import Thread
from time import sleep


def calculate_potency(waiting_time, number, potency, name, potency_name): # Calculate to the potency
    print(f"Task startup of {name}, calculate {number} to the {potency_name}: {number**potency}")
    sleep(waiting_time)
    print(f"Completion of task {name}")


lista_thread = [] # List criation
lista_thread.append(Thread(target=calculate_potency, args=(3, 4, 3, "A", "cube")))# Add thread to list
lista_thread.append(Thread(target=calculate_potency, args=(2, 4, 2, "B", "square"))) # Also add
for thread in lista_thread: #Initilization of each list
    thread.start()
for thread in lista_thread: # wait each list ends
    thread.join()
print("The execution has completed")
