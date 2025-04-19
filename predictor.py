import numpy as np
from tensorflow.keras.models import load_model

model = load_model("model/aviator_model.h5")

def prever(dados):
    entrada = np.array(dados[-10:]).reshape(1, 10)
    previsao = model.predict(entrada)[0][0]
    return round(float(previsao), 2)
