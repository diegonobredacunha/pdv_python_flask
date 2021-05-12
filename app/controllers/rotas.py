from flask import render_template, request
from app import app
from sqlalchemy.sql import select, and_, or_
from app.controllers import pessoa_controller as pc

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listar/pessoas')
def listar_pessoas():
    pessoas = pc.selecionar_todos()
    
    return render_template('listar_pessoas.html', pessoas=pessoas, ordem='nome')

@app.route('/ordenar_pessoas/<campo>/<ordem_anterior>')
def ordenar_pessoas(campo='nome', ordem_anterior=''):
    pessoas = pc.ordenar(campo, ordem_anterior)

    return render_template('listar_pessoas.html', pessoas=pessoas, ordem=campo)

@app.route('/consultar_pessoas', methods=['POST'])
def consultar_pessoas():
    consulta = '%' + request.form.get('consulta') + '%'
    campo = request.form.get('campo')
    pessoas = pc.consultar_todos(campo, consulta)

    return render_template('listar_pessoas.html', pessoas=pessoas, ordem='nome')

@app.route('/nova/pessoa')
def nova_pessoa():
    return render_template('nova_pessoa.html')