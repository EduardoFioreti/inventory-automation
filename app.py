from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para armazenar os produtos na memória (enquanto o servidor estiver rodando)
lista_produtos = []

@app.route('/')
def index():
    # Passamos a lista para o HTML exibir na tabela
    return render_template('index.html', produtos=lista_produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # Coletando todos os 7 campos que o robô vai enviar
    codigo = request.form.get('codigo')
    marca = request.form.get('marca')
    tipo = request.form.get('tipo')
    categoria = request.form.get('categoria')
    preco = float(request.form.get('preco'))
    custo = float(request.form.get('custo'))
    obs = request.form.get('obs')

    # Cálculo extra: Lucro (útil para análise de dados futuramente)
    lucro = round(preco - custo, 2)

    # Criando o dicionário do produto
    novo_produto = {
        'codigo': codigo,
        'marca': marca,
        'tipo': tipo,
        'categoria': categoria,
        'preco': preco,
        'custo': custo,
        'lucro': lucro,
        'obs': obs if obs else "-"
    }

    # Adiciona no topo da lista para você ver o último cadastrado primeiro
    lista_produtos.insert(0, novo_produto)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)