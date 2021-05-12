from app.models.tabelas import Pessoa

def selecionar_todos():
    return Pessoa.query.all()

def ordenar(campo, ordem_anterior):
    if campo == 'nome':
        if ordem_anterior == campo:
            return Pessoa.query.order_by(Pessoa.nome.desc()).all()
        else:
            return Pessoa.query.order_by(Pessoa.nome).all()
    elif campo == 'cpf':
        if ordem_anterior == campo:
            return Pessoa.query.order_by(Pessoa.cpf.desc()).all()
        else:
            return Pessoa.query.order_by(Pessoa.cpf).all()
    else:
        return Pessoa.query.order_by(Pessoa.nome).all()

def consultar_todos(campo, consulta):
    consulta = consulta.upper()

    if campo == 'nome':
        return Pessoa.query.filter(Pessoa.nome.like(consulta)).all()
    elif campo == 'cpf':
        return Pessoa.query.filter(Pessoa.cpf.like(consulta)).all()
    else:
        return Pessoa.query.all()