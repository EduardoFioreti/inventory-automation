from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# --- CONFIGURAÇÃO ATUALIZADA PARA OPERA GX ---
options = Options()
options.binary_location = r"C:\Users\Eduardo Fioreti\AppData\Local\Programs\Opera GX\opera.exe"

# Forçamos o download da versão mais recente do driver compatível com seu navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

try:
    # O restante do seu código continua igual...
    navegador.get("http://127.0.0.1:5000")
    # ...
    time.sleep(2)

    # 2. Lê a sua lista de produtos
    tabela = pd.read_csv("produtos.csv")

    # 3. Loop de Cadastro Profissional
    for linha in tabela.index:
        codigo = str(tabela.loc[linha, "codigo"])
        marca = str(tabela.loc[linha, "marca"])

        # Localizando pelos IDs exatos que você criou no Passo 5
        navegador.find_element(By.ID, "id_codigo").send_keys(codigo)
        navegador.find_element(By.ID, "id_marca").send_keys(marca)
        
        # Clica no botão de enviar
        navegador.find_element(By.ID, "btn_enviar").click()
        
        print(f"Sucesso: Produto {codigo} cadastrado!")
        time.sleep(0.5)

finally:
    print("\n--- Automação Finalizada com Sucesso! ---")
    # navegador.quit() # Remova o '#' se quiser que o navegador feche sozinho no fim