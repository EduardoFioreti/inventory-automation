from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

try:
    navegador.get("https://projeto-cadastro-lake.vercel.app")
    time.sleep(3)

    tabela = pd.read_csv("produtos.csv")

    for linha in tabela.index:
        # Preenchendo todos os campos do CSV
        navegador.find_element(By.ID, "id_codigo").send_keys(str(tabela.loc[linha, "codigo"]))
        navegador.find_element(By.ID, "id_marca").send_keys(str(tabela.loc[linha, "marca"]))
        navegador.find_element(By.ID, "id_tipo").send_keys(str(tabela.loc[linha, "tipo"]))
        navegador.find_element(By.ID, "id_categoria").send_keys(str(tabela.loc[linha, "categoria"]))
        navegador.find_element(By.ID, "id_preco").send_keys(str(tabela.loc[linha, "preco_unitario"]))
        navegador.find_element(By.ID, "id_custo").send_keys(str(tabela.loc[linha, "custo"]))
        
        # Obs pode estar vazio, então tratamos
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            navegador.find_element(By.ID, "id_obs").send_keys(obs)

        navegador.find_element(By.ID, "btn_enviar").click()
        print(f"Cadastrado: {tabela.loc[linha, 'codigo']}")
        time.sleep(0.3)

finally:
    print("Automação concluída!")