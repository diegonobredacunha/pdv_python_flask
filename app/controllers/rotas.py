from flask import render_template, request
from app import app, db
from app.models.tabelas import Pessoa, Funcionario, Contato
from sqlalchemy.sql import select, and_, or_

@app.route('/')
def home():
    return 'bosta seca'

@app.route('/lista/pessoas')
def lista_funcionarios():
    funcionarios = select(Funcionario.query.all()).select_from(Funcionario.outerjoin(Pessoa.query.all()))
    return render_template('lista_funcionarios.html', funcionarios=funcionarios, ordem='id')
    


