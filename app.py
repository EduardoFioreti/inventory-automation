from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# Banco de dados temporário na memória
banco_de_produtos = []

@app.route('/')
def index():
    return render_template('index.html', lista=banco_de_produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    codigo = request.form.get('codigo')
    marca = request.form.get('marca')
    if codigo:
        banco_de_produtos.append({'codigo': codigo, 'marca': marca})
    return redirect('/')

# No final do seu arquivo app.py
app = app # Isso ajuda o Vercel a encontrar a instância do Flask

if __name__ == '__main__':
    app.run(debug=True)
    # No final do arquivo, mude para:
app = app