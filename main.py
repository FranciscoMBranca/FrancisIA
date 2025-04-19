from scraper import coletar_resultados_aviator
from predictor import prever

dados = coletar_resultados_aviator()
resultado = prever(dados)
print("Previsão TensorFlow:", resultado)
