# 🚀 Sistema de Gestão de Inventário com Automação Robótica (RPA)

Este projeto une **Desenvolvimento Web** com **Automação de Processos (RPA)**. O sistema consiste em uma plataforma de cadastro de produtos integrada a um robô que realiza o preenchimento em massa de dados a partir de arquivos CSV.

> **Status do Projeto:** 🟢 Produção (Vercel)
> **Link do Sistema:** [projeto-cadastro-lake.vercel.app](https://projeto-cadastro-lake.vercel.app/)

---

## 📸 Interface

![Controle de Inventário](screenshot.png)

---

## 🛠️ Tecnologias Utilizadas

### Backend & Web
* **Python / Flask** — Estrutura do servidor e rotas da aplicação
* **HTML5 & CSS3 (Bootstrap 5)** — Interface responsiva e moderna
* **Vercel** — Cloud hosting para o deploy da aplicação

### Automação (RPA)
* **Selenium WebDriver** — Motor de automação para interação com o navegador
* **Pandas** — Manipulação e leitura de dados do arquivo CSV
* **Keyboard** — Controle de fluxo e interrupção via tecla de atalho (`ESC`)
* **WebDriver Manager** — Gestão automática de drivers do Chrome

---

## 📋 Funcionalidades

* **CRUD Completo** — Criação, leitura, edição e exclusão de produtos na interface
* **Automação em Massa** — O robô lê uma lista CSV e cadastra os produtos automaticamente, simulando comportamento humano em alta velocidade
* **Análise de Margens** — Visualização dinâmica de preços e custos para controle financeiro
* **Controle de Fluxo** — Botão de reset de lista e sistema de segurança para pausar o robô a qualquer momento via `ESC`

---

## 🚀 Como Executar

### 1. Clone o repositório
git clone [https://github.com/EduardoFioreti/inventory-automation.git](https://github.com/EduardoFioreti/inventory-automation.git)
cd inventory-automation
---
2. Instale as dependências:
pip install -r requirements.txt
---
3. Inicie o servidor:
python app.py
---
4. Acesse no navegador:
http://localhost:5000
---
5. Para rodar a automação RPA
Com o servidor rodando, abra outro terminal e execute:
python automacao_web.py
---
💡 O robô vai ler o arquivo produtos.csv e cadastrar os itens automaticamente. Pressione ESC a qualquer momento para interromper a execução.
---
📁 Estrutura do Projeto
inventory-automation/
├── app.py                # Servidor Flask e rotas da aplicação
├── automacao_web.py      # Script de automação RPA (Selenium)
├── produtos.csv          # Lista de produtos base para a automação
├── requirements.txt      # Dependências e bibliotecas do projeto
├── templates/            # Páginas e interfaces HTML (Jinja2)
└── vercel.json           # Configurações de deploy na nuvem
---
👨‍💻 Autor
Eduardo Fioreti
---
🔗 LinkedIn: linkedin.com/in/eduardo-fioreti-4a8931371
📧 Email: eduardofioretidev@gmail.com
