# 🚀 Sistema de Gestão de Inventário com Automação Robótica (RPA)

Este projeto une o poder do **Desenvolvimento Web** com a **Automação de Processos (RPA)**. O sistema consiste em uma plataforma de cadastro de produtos integrada a um robô que realiza o preenchimento em massa de dados a partir de arquivos CSV.

> **Status do Projeto:** 🟢 Produção (Vercel)  
> **Link do Sistema:** [projeto-cadastro-lake.vercel.app](https://projeto-cadastro-lake.vercel.app/)

---

## 🛠️ Tecnologias Utilizadas

### **Backend & Web**
* **Python / Flask:** Estrutura do servidor e rotas da aplicação.
* **HTML5 & CSS3 (Bootstrap 5):** Interface responsiva e moderna.
* **Vercel:** Cloud hosting para o deploy da aplicação.

### **Automação (RPA)**
* **Selenium WebDriver:** Motor de automação para interação com o navegador.
* **Pandas:** Manipulação e análise de dados do arquivo CSV.
* **Keyboard:** Controle de fluxo e interrupção via tecla de atalho (`ESC`).
* **WebDriver Manager:** Gestão automática de drivers do Chrome.

---

## 📋 Funcionalidades Principais

1.  **CRUD Completo:** Criação, leitura, edição e exclusão de produtos diretamente na interface.
2.  **Automação em Massa:** O robô lê uma lista de produtos e os cadastra automaticamente em tela cheia, simulando o comportamento humano em alta velocidade.
3.  **Análise de Margens:** Visualização dinâmica de preços (Verde) e custos (Vermelho) para facilitar o controle financeiro.
4.  **Controle de Fluxo:** Implementação de botão de "Reset de Lista" e sistema de segurança para pausar o robô a qualquer momento.

---

## 🚀 Como Executar o Robô

1. Clone o repositório:
   ```bash
   git clone [https://github.com/EduardoFioreti/ProjetoCadastro.git](https://github.com/EduardoFioreti/ProjetoCadastro.git)
