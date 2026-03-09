from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Para simular o Enter
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Configuração para manter o navegador aberto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

try:
    # 1. Acesso ao site
    navegador.get("https://projeto-cadastro-lake.vercel.app/")
    time.sleep(3) # Tempo de segurança para carregar o servidor da Vercel

    # 2. Leitura dos dados
    tabela = pd.read_csv("produtos.csv")

    for linha in tabela.index:
        # Preenchimento dos campos
        navegador.find_element(By.ID, "id_codigo").send_keys(str(tabela.loc[linha, "codigo"]))
        navegador.find_element(By.ID, "id_marca").send_keys(str(tabela.loc[linha, "marca"]))
        navegador.find_element(By.ID, "id_tipo").send_keys(str(tabela.loc[linha, "tipo"]))
        navegador.find_element(By.ID, "id_categoria").send_keys(str(tabela.loc[linha, "categoria"]))
        navegador.find_element(By.ID, "id_preco").send_keys(str(tabela.loc[linha, "preco_unitario"]))
        navegador.find_element(By.ID, "id_custo").send_keys(str(tabela.loc[linha, "custo"]))
        
        # Campo de Observação com tratamento de erro
        campo_obs = navegador.find_element(By.ID, "id_obs")
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            campo_obs.send_keys(obs)

        # ESTRATÉGIA DE ENVIO: Enviar o comando ENTER no último campo preenchido
        # Isso substitui o clique no botão e é muito mais estável
        campo_obs.send_keys(Keys.ENTER)
        
        print(f"Enviado: {tabela.loc[linha, 'codigo']}")
        
        # Espera o site recarregar para a lista atualizar antes da próxima linha
        time.sleep(1.5) 

except Exception as e:
    print(f"Erro na automação: {e}")

finally:
    print("\n--- Automação concluída no Chrome! ---")