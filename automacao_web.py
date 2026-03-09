import os
import time
import keyboard
import csv
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

try:
    subprocess.run("taskkill /f /im chromedriver.exe /t", shell=True, capture_output=True)
    subprocess.run("taskkill /f /im chrome.exe /t", shell=True, capture_output=True)
except:
    pass

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--log-level=3")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_atual, "produtos.csv")

try:
    print("Iniciando o navegador... Aguarde a tela branca sumir.")
    
    navegador = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    url_site = "https://projeto-cadastro-lake.vercel.app/"
    for i in range(3):
        print(f"Tentativa {i+1} de carregar o site...")
        navegador.get(url_site)
        time.sleep(5)
        if "vercel.app" in navegador.current_url:
            break

    print("Site carregado! Preparando dados do CSV...")
    
    if not os.path.exists(caminho_csv):
        print(f"ERRO: Arquivo {caminho_csv} não encontrado!")
    else:
        with open(caminho_csv, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            print("Automação iniciada. Pressione ESC para parar.")
            
            for linha in leitor:
                if keyboard.is_pressed('esc'):
                    print("Interrompido pelo usuário.")
                    break

                navegador.find_element(By.ID, "id_codigo").send_keys(linha["codigo"])
                navegador.find_element(By.ID, "id_marca").send_keys(linha["marca"])
                navegador.find_element(By.ID, "id_tipo").send_keys(linha["tipo"])
                navegador.find_element(By.ID, "id_categoria").send_keys(linha["categoria"])
                navegador.find_element(By.ID, "id_preco").send_keys(linha["preco_unitario"])
                navegador.find_element(By.ID, "id_custo").send_keys(linha["custo"])
                
                obs = linha.get("obs", "")
                campo_obs = navegador.find_element(By.ID, "id_obs")
                if obs and obs.lower() != "nan":
                    campo_obs.send_keys(obs)

                campo_obs.send_keys(Keys.ENTER)
                
                print(f"Cadastrado: {linha['codigo']}")
                time.sleep(2.5)

except Exception as e:
    print(f"\nErro encontrado: {e}")
    print("\nDICA: Se a tela continuou branca, desative o antivírus por 5 minutos.")

finally:
    print("\nScript finalizado.")