from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__) 

@cliente_route.route('/')
def lista_cliente():
    """Listar os clientes"""
    return render_template('lista_cliente.html', clientes=CLIENTES)

@cliente_route.route('/', methods = ['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente no site """
    pass

@cliente_route.route('/new')
def form_cliente():
    """ Formulario para cadastrar um cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir cliente """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def editar_cliente(cliente_id):
    """ Renderizar Cliente """
    return render_template('editar_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar Cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ Excluir Cliente """
    pass
