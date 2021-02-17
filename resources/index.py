from flask_restful import Resource
from flask import make_response, render_template
from model.pets import lista_pets

class Index(Resource):
    def get(self, nome='Usuário'):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', nome_usuario=nome, lista_pets=lista_pets),200,headers) # no return padrao de um verbo http eh um json o "make_response" do Flask customiza o headers, nesse caso ele faz o browser entender que eh um html

