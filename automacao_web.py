from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# --- CONFIGURAÇÃO PARA O CHROME NÃO FECHAR ---
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

try:
    # 1. Acessa o seu site na Vercel
    navegador.get("https://projeto-cadastro-lake.vercel.app/")
    time.sleep(3) # Tempo para o site carregar na Vercel

    # 2. Carrega o CSV
    tabela = pd.read_csv("produtos.csv")

    # 3. Loop de Automação
    for linha in tabela.index:
        # Preenchendo cada campo pelo ID que está no seu index.html
        navegador.find_element(By.ID, "id_codigo").send_keys(str(tabela.loc[linha, "codigo"]))
        navegador.find_element(By.ID, "id_marca").send_keys(str(tabela.loc[linha, "marca"]))
        navegador.find_element(By.ID, "id_tipo").send_keys(str(tabela.loc[linha, "tipo"]))
        navegador.find_element(By.ID, "id_categoria").send_keys(str(tabela.loc[linha, "categoria"]))
        
        # Atenção ao nome da coluna no seu CSV: preco_unitario
        navegador.find_element(By.ID, "id_preco").send_keys(str(tabela.loc[linha, "preco_unitario"]))
        navegador.find_element(By.ID, "id_custo").send_keys(str(tabela.loc[linha, "custo"]))
        
        # Tratando a observação
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            navegador.find_element(By.ID, "id_obs").send_keys(obs)

        # Clica no botão de enviar
        navegador.find_element(By.ID, "btn_enviar").click()
        
        print(f"Sucesso: {tabela.loc[linha, 'codigo']} cadastrado!")
        
        # Espera curta para o site processar o cadastro antes do próximo
        time.sleep(0.5)

except Exception as e:
    print(f"Ocorreu um erro durante a automação: {e}")

finally:
    print("\n--- Processo finalizado! O navegador permanecerá aberto para conferência. ---")