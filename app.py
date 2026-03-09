from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista na memória para armazenar os produtos temporariamente
lista_produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=lista_produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # Coletando os 7 campos enviados pelo robô ou formulário
    novo_item = {
        'codigo': request.form.get('codigo'),
        'marca': request.form.get('marca'),
        'tipo': request.form.get('tipo'),
        'categoria': request.form.get('categoria'),
        'preco': request.form.get('preco'),
        'custo': request.form.get('custo'),
        'obs': request.form.get('obs') if request.form.get('obs') else "-"
    }
    
    # Adiciona no topo da lista
    lista_produtos.insert(0, novo_item)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)