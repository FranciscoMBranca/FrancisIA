import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from scraper import coletar_resultados_aviator

def gerar_treinamento(lista):
    X, y = [], []
    for i in range(len(lista) - 10):
        X.append(lista[i:i+10])
        y.append(lista[i+10])
    return np.array(X), np.array(y)

def treinar():
    dados = coletar_resultados_aviator()
    X, y = gerar_treinamento(dados)
    model = Sequential()
    model.add(Dense(64, input_dim=10, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mse', optimizer='adam')
    model.fit(X, y, epochs=100, verbose=1)
    model.save("model/aviator_model.h5")

if __name__ == "__main__":
    treinar()
