# 🤖 Inventory Automation — Sistema de Gestão de Inventário com Automação Robótica (RPA)

Aplicação web para gerenciamento de produtos integrada a um robô de automação capaz de realizar cadastros em massa a partir de arquivos CSV.

O projeto combina conceitos de **Desenvolvimento Web**, **Automação de Processos (RPA)**, **Manipulação de Dados** e **Integração entre Sistemas**, utilizando Python como linguagem principal.

🔗 **Sistema Online:** https://projeto-cadastro-lake.vercel.app/

> 🚀 Projeto publicado em produção utilizando Vercel.

---

## 🎯 Objetivo do Projeto

Empresas frequentemente precisam cadastrar centenas de produtos em sistemas internos.

Este projeto foi desenvolvido para automatizar esse processo através de um robô que lê informações de arquivos CSV e realiza os cadastros automaticamente, reduzindo erros manuais e aumentando a produtividade operacional.

---

## 🚀 Tecnologias Utilizadas

| Camada               | Tecnologia         |
| -------------------- | ------------------ |
| Backend              | Flask              |
| Frontend             | HTML5              |
| Estilização          | CSS3 + Bootstrap 5 |
| Automação RPA        | Selenium WebDriver |
| Manipulação de Dados | Pandas             |
| Controle de Execução | Keyboard           |
| Drivers              | WebDriver Manager  |
| Deploy               | Vercel             |
| Versionamento        | Git + GitHub       |

---

## 📋 Funcionalidades

### 📦 Gestão de Produtos

* Cadastro de produtos
* Edição de registros
* Exclusão de produtos
* Consulta de inventário
* Controle de preços e custos

### 📊 Análise Financeira

* Visualização de custos
* Controle de margem de lucro
* Comparação de preços
* Organização de dados para tomada de decisão

### 🤖 Automação Robótica (RPA)

O robô realiza automaticamente:

* Leitura de arquivos CSV
* Preenchimento de formulários web
* Cadastro em massa de produtos
* Navegação automatizada entre páginas
* Tratamento de fluxo operacional

### 🛑 Controle de Segurança

* Interrupção imediata através da tecla ESC
* Reset automático de listas
* Encerramento seguro da execução

---

## 🏗️ Arquitetura da Aplicação

```text
Arquivo CSV
      ↓
    Pandas
      ↓
Automação Selenium
      ↓
Sistema Flask
      ↓
Banco de Dados
```

A arquitetura foi projetada para demonstrar a integração entre sistemas web e automação de processos empresariais.

---

## 📁 Estrutura do Projeto

```text
inventory-automation/
│
├── app.py
│   └── Aplicação Flask
│
├── automacao_web.py
│   └── Robô de automação RPA
│
├── produtos.csv
│   └── Dados utilizados pelo robô
│
├── requirements.txt
│   └── Dependências do projeto
│
├── templates/
│   └── Interfaces HTML
│
├── static/
│   └── Arquivos CSS
│
└── vercel.json
    └── Configuração de deploy
```

---

## ⚙️ Fluxo da Automação

O processo automatizado segue as etapas:

1. Leitura do arquivo CSV
2. Conversão dos dados utilizando Pandas
3. Inicialização do navegador pelo Selenium
4. Navegação até o formulário web
5. Preenchimento automático dos campos
6. Envio das informações
7. Repetição do processo para todos os registros

---

## 💡 Conceitos Aplicados

Durante o desenvolvimento foram utilizados:

* Desenvolvimento Web com Flask
* Arquitetura MVC
* Automação Robótica de Processos (RPA)
* Manipulação de dados com Pandas
* Automação de navegador com Selenium
* Tratamento de exceções
* Integração entre aplicações
* Deploy em ambiente de produção

---

## 🚀 Como Executar Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/EduardoFioreti/inventory-automation.git

cd inventory-automation
```

### 2. Criar Ambiente Virtual

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
python app.py
```

### 5. Acessar o Sistema

```text
http://localhost:5000
```

---

## 🤖 Executando a Automação

Com a aplicação em execução, abra um novo terminal e execute:

```bash
python automacao_web.py
```

O robô irá:

* Ler o arquivo produtos.csv
* Abrir o navegador automaticamente
* Preencher os formulários
* Realizar os cadastros em massa

Para interromper a execução:

```text
Pressione ESC
```

---

## 📸 Screenshots

### Dashboard

```text
screenshots/dashboard.png
```

### Cadastro de Produtos

```text
screenshots/cadastro.png
```

### Automação em Execução

```text
screenshots/automacao.png
```

---

## 🔮 Roadmap

* [ ] Upload de CSV pela interface
* [ ] Dashboard analítico
* [ ] Histórico de execuções
* [ ] Logs detalhados da automação
* [ ] Integração com banco MySQL
* [ ] Dockerização da aplicação
* [ ] Agendamento automático de execuções

---

## 👨‍💻 Autor

**Eduardo Fioreti**

🎓 Engenharia da Computação — UniCEUMA

🔗 GitHub: https://github.com/EduardoFioreti

💼 LinkedIn: https://linkedin.com/in/eduardo-fioreti-4a8931371

📧 E-mail: [eduardofioretidev@gmail.com](mailto:eduardofioretidev@gmail.com)
