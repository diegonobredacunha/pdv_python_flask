import datetime
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
    titulo = db.Column(db.String(20))
    zona = db.Column(db.String(20))
    secao = db.Column(db.String(20))
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Float, nullable=False)
    
    pessoa_id = db.Column(db.BigInteger, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoa', back_populates='funcionarios')
    usuario = relationship('Usuario', uselist=False, back_populates='funcionarios')
    despesa_rendimento = relationship('DespesaRendimento', uselist=False, back_populates='funcionarios')
    caixa = relationship('Caixa', uselist=False, back_populates='funcionarios')

    def __init__(self, matricula, dt_admissao, cargo, salario, pessoa_id, dt_desligamento=None, ctps=None, serie=None, titulo=None, zona=None, secao=None):
        self.matricula = matricula
        self.dt_admissao = dt_admissao
        self.dt_desligamento = dt_desligamento
        self.ctps = ctps
        self.serie = serie
        self.titulo = titulo
        self.zona = zona
        self.secao = secao
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
        return '<Endereco %r>' % self.logradouro

class TipoUsuario(db.Model):
    __tablename__ = 'tipos_usuarios'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(20))
    
    usuario = relationship('Usuario', uselist=False, back_populates='tipos_usuarios')

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return '<TipoUsuario %r>' % self.descricao

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.BigInteger, primary_key=True)
    senha = db.Column(db.String(20))
    
    tipo_usuario_id = db.Column(db.Integer, ForeignKey('tipos_usuarios.id'))
    tipo_usuario = relationship('TipoUsuario', back_populates='usuarios')
    funcionario_id = db.Column(db.BigInteger, ForeignKey('funcionarios.id'))
    funcionario = relationship('Funcionario', back_populates='usuarios')

    def __init__(self, senha, tipo_usuario_id, funcionario_id):
        self.senha = senha
        self.tipo_usuario_id = tipo_usuario_id
        self.funcionario_id = funcionario_id

    def __repr__(self):
        return '<Usuario: %r>' % self.id

class TipoDespesaRendimento(db.Model):
    __tablename__ = 'tipos_despesas_rendimentos'

    id = db.Column(db.BigInteger, primary_key=True)
    descricao = db.Column(db.String(20))
    
    despesa_rendimento = relationship('DespesaRendimento', uselist=False, back_populates='tipos_despesas_rendimentos')

    def __init__(self, descricao):
        self.descricao = descricao
    
    def __repr__(self):
        return '<TipoDespesaRendimento %r>' % self.descricao

class DespesaRendimento(db.Model):
    __tablename__ = 'despesas_rendimentos'

    id = db.Column(db.BigInteger, primary_key=True)
    descricao = db.Column(db.String(255))
    valor = db.Column(db.Float)
    
    tipo_despesa_rendimento_id = db.Column(db.BigInteger, ForeignKey('tipos_despesas_rendimentos.id'))
    tipo_despesa_rendimento = relationship('TipoDespesaRendimento', back_populates='despesas_rendimentos')
    funcionario_id = db.Column(db.BigInteger, ForeignKey('funcionarios.id'))
    funcionario = relationship('Funcionario', back_populates='despesas_rendimentos')

    def __init__(self, descricao, valor, tipo_despesa_rendimento_id, funcionario_id):
        self.descricao = descricao
        self.valor = valor
        self.tipo_despesa_rendimento_id = tipo_despesa_rendimento_id
        self.funcionario_id = funcionario_id
    
    def __repr__(self):
        return '<DespesaRendimento %r>' % self.descricao
    
class Caixa(db.Model):
    __tablename__ = 'caixas'

    id = db.Column(db.BigInteger, primary_key=True)
    dt_rendimento = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    funcionario_id = db.Column(db.BigInteger, ForeignKey('funcionarios.id'))
    funcionario = relationship('Funcionario', back_populates='caixas')
    produto_caixa = relationship('ProdutoCaixa', uselist=False, back_populates='caixas')

    def __init__(self, dt_rendimento, funcionario_id):
        self.dt_rendimento = dt_rendimento
        self.funcionario_id = funcionario_id
    
    def __repr__(self):
        return '<Caixa %r>' % self.dt_rendimento
    
class Produto(db.Model):
    __tablename__ = 'produtos'
    
    id = db.Column(db.BigInteger, primary_key=True)
    codigo_barra = db.Column(db.String(255), unique=True)
    descricao = db.Column(db.String(100))
    quantidade = db.Column(db.Integer, nullable=False)
    valor_unitario = db.Column(db.Float(16,2), nullable=False)
    preco_venda = db.Column(db.Float(16,2), nullable=False)
    
    produto_caixa = relationship('ProdutoCaixa', uselist=False, back_populates='produtos')
    
    def __init__(self, codigo_barra, descricao, quantidade, valor_unitario, preco_venda):
        self.codigo_barra = codigo_barra
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.preco_venda = preco_venda
    
    def __repr__(self):
        return '<Produto %r>' % self.descricao

class ProdutoCaixa(db.Model):
    __tablename__ = 'produtos_caixa'
    
    id = db.Column(db.BigInteger, primary_key=True)
    quantidade_produto_comprado = db.Column(db.Integer, nullable=False)
    total_compra = db.Column(db.Float(16,2), nullable=False)
    
    produto_id = db.Column(db.BigInteger, ForeignKey('produtos.id'))
    produto = relationship('Produto', back_populates='produtos_caixa')
    caixa_id = db.Column(db.BigInteger, ForeignKey('caixas.id'))
    caixa = relationship('Caixa', back_populates='produtos_caixa')
    
    def __init__(self, quantidade_produto_comprado, total_compra, produto_id, caixa_id):
        self.quantidade_produto_comprado = quantidade_produto_comprado
        self.total_compra = total_compra
        self.produto_id = produto_id
        self.caixa_id = caixa_id
