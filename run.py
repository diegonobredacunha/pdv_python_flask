from app import manager

if __name__ == '__main__':
    manager.run()

'''
from flask import Flask
from sqlalchemy import Column,BigInteger,Integer,String
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/pdv'
db = SQLAlchemy(app)
app.debug = True

class Pessoa(db.Model):
    id = db.Column(BigInteger, primary_key=True)
    nome = db.Column(String(100))
    cpf = db.Column(String(11), unique=True)

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        return '<Pessoa %r>' % self.nome

@app.route('/')
def index():
    return 'funfando'

if __name__ == "__main__":
    app.run()
'''