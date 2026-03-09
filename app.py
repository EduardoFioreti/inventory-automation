from flask import Flask, render_template, request, redirect

app = Flask(__name__)
lista_produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=lista_produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    codigo = request.form.get('codigo')
    
    # Lógica de Edição: Se o código já existe, remove o antigo antes de inserir o novo
    for i, p in enumerate(lista_produtos):
        if p['codigo'] == codigo:
            lista_produtos.pop(i)
            break

    novo_item = {
        'codigo': codigo,
        'marca': request.form.get('marca'),
        'tipo': request.form.get('tipo'),
        'categoria': request.form.get('categoria'),
        'preco': request.form.get('preco'),
        'custo': request.form.get('custo'),
        'obs': request.form.get('obs') if request.form.get('obs') else "-"
    }
    lista_produtos.insert(0, novo_item)
    return redirect('/')

# --- NOVA ROTA: EXCLUIR ---
@app.route('/excluir/<codigo>')
def excluir(codigo):
    global lista_produtos
    lista_produtos = [p for p in lista_produtos if p['codigo'] != codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

    # --- NOVA ROTA: LIMPAR TUDO ---
@app.route('/limpar_tudo')
def limpar_tudo():
    global lista_produtos
    lista_produtos = []
    return redirect('/')