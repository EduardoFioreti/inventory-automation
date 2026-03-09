from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import keyboard  # Biblioteca para detectar a tecla de pausa

# Configuração do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# --- MELHORIA: TELA CHEIA ---
navegador.maximize_window()

try:
    navegador.get("https://projeto-cadastro-lake.vercel.app/")
    time.sleep(3)

    tabela = pd.read_csv("produtos.csv")

    print("Automação iniciada! Pressione 'ESC' a qualquer momento para pausar/parar.")

    for linha in tabela.index:
        # --- MELHORIA: TECLA DE PAUSA (ESC) ---
        if keyboard.is_pressed('esc'):
            print(f"\n[PAUSA] Automação interrompida pelo usuário no item: {tabela.loc[linha, 'codigo']}")
            break

        # Preenchimento dos campos
        navegador.find_element(By.ID, "id_codigo").send_keys(str(tabela.loc[linha, "codigo"]))
        navegador.find_element(By.ID, "id_marca").send_keys(str(tabela.loc[linha, "marca"]))
        navegador.find_element(By.ID, "id_tipo").send_keys(str(tabela.loc[linha, "tipo"]))
        navegador.find_element(By.ID, "id_categoria").send_keys(str(tabela.loc[linha, "categoria"]))
        navegador.find_element(By.ID, "id_preco").send_keys(str(tabela.loc[linha, "preco_unitario"]))
        navegador.find_element(By.ID, "id_custo").send_keys(str(tabela.loc[linha, "custo"]))
        
        campo_obs = navegador.find_element(By.ID, "id_obs")
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            campo_obs.send_keys(obs)

        # Envia com Enter
        campo_obs.send_keys(Keys.ENTER)
        
        print(f"Cadastrado: {tabela.loc[linha, 'codigo']}")
        
        # Espera o site processar
        time.sleep(1.2) 

except Exception as e:
    print(f"Erro: {e}")

finally:
    print("\n--- Script finalizado. ---")