from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pessoa(db.Model):
    __tablename__ = 'pessoas'

    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    dt_nascimento = db.Column(db.Date)
    sexo = db.Column(db.String(1))
    estado_civil = db.Column(db.String(20))
    nm_mae = db.Column(db.String(100))
    nm_pai = db.Column(db.String(100))
    funcionario = relationship('Funcionario', uselist=False, back_populates='pessoas')
    contato = relationship('Contato')
    endereco = relationship('Endereco')
  
    def __init__(self, nome, cpf, dt_nascimento=None, sexo=None, estado_civil=None, logradouro=None, nu_logradouro=None, complemento=None, bairro=None, cep=None, cidade=None, uf=None):
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.logradouro = logradouro
        self.nu_logradouro = nu_logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
    
    def __repr__(self):
        return '<Pessoa %r>' % self.nome

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.BigInteger, primary_key=True)
    matricula = db.Column(db.String(10), nullable=False, unique=True)
    dt_admissao = db.Column(db.Date, nullable=False)
    dt_desligamento = db.Column(db.Date)
    ctps = db.Column(db.String(20))
    serie = db.Column(db.String(20))
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Float, nullable=False)
    pessoa_id = db.Column(db.BigInteger, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoa', back_populates='funcionarios')

    def __init__(self, matricula, dt_admissao, cargo, salario, pessoa_id, dt_desligamento=None, ctps=None, serie=None):
        self.matricula = matricula
        self.dt_admissao = dt_admissao
        self.dt_desligamento = dt_desligamento
        self.ctps = ctps
        self.serie = serie
        self.cargo = cargo
        self.salario = salario
        self.pessoa_id = pessoa_id
    
    def __repr__(self):
        return '<Funcionario %r>' % self.matricula

class Contato(db.Model):
    __tablename__ = 'contatos'

    id = db.Column(db.BigInteger, primary_key=True)
    ddd = db.Column(db.String(2))
    telefone = db.Column(db.String(10))
    email = db.Column(db.String(100))
    pessoa_id = db.Column(db.BigInteger, ForeignKey('pessoas.id'))

    def __init__(self, ddd=None, telefone=None, email=None, pessoa_id=None):
        self.ddd = ddd
        self.telefone = telefone
        self.email = email
        self.pessoa_id = pessoa_id
    
    def __repr__(self):
        return '<Contato %r>' % self.email

class Endereco(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column(db.BigInteger, primary_key=True)
    logradouro = db.Column(db.String(100))
    nu_logradouro = db.Column(db.String(5))
    complemento = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50))
    uf = db.Column(db.String(2))
    pessoa_id = db.Column(db.BigInteger, ForeignKey('pessoas.id'))

    def __init__(self, logradouro=None, nu_logradouro=None, complemento=None, bairro=None, cep=None, cidade=None, uf=None, pessoa_id=None):
        self.logradouro = logradouro
        self.nu_logradouro = nu_logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
        self.pessoa_id = pessoa_id
    
    def __repr__(self):
        return '<Pessoa %r>' % self.nome    
