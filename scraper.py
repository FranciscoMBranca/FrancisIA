from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def coletar_resultados_aviator():
    url = "https://aviatorgames.ai/demo-game?game=aviator"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10)
    resultados = []
    while len(resultados) < 150:
        spans = driver.find_elements(By.CLASS_NAME, "coefficient")
        for span in spans:
            try:
                valor = float(span.text.replace("x", "").strip())
                if valor not in resultados:
                    resultados.append(valor)
            except:
                continue
        time.sleep(2)
    driver.quit()
    return resultados[:150]
