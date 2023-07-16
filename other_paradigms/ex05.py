# # Data Processing
# import numpy as np
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# x = np.array([5,10,15,20,25,30]).reshape((-1,1))
# y = np.array([6,12,14,23,27,32])

# model = LinearRegression().fit(x,y)

# # Predict aa response and print it:
# y_pred = model.predict(x)
# print("Test datas:", y, sep="\n")
# print("Prediction datas:", y_pred, sep="\n")

# plt.scatter(x,y,c="blue")
# plt.plot(x,y_pred,c="red")
# plt.legend(["Prediction", "Real"])
# plt.show()

# Exercício 01 = carregar dados da base load_digts. Informar a quantidade de dados
from sklearn.datasets import load_digits
digitos = load_digits()

print(f"Shape dos dados de imagens: {digitos.data.shape}")
print(f"Shape dos dados rotulados: {digitos.target.shape}")

# Exercício 02 - Vizualizar os dados que foram carregados
