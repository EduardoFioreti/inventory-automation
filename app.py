from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para salvar os produtos durante a sessão (limpa se o servidor reiniciar)
lista_produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=lista_produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # Coletando os 7 campos do formulário
    novo_item = {
        'codigo': request.form.get('codigo'),
        'marca': request.form.get('marca'),
        'tipo': request.form.get('tipo'),
        'categoria': request.form.get('categoria'),
        'preco': request.form.get('preco'),
        'custo': request.form.get('custo'),
        'obs': request.form.get('obs') if request.form.get('obs') else "-"
    }
    
    # Adicionando no topo da lista para visualização imediata
    lista_produtos.insert(0, novo_item)
    
    # Importante: Redireciona de volta para a home para limpar o formulário
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)