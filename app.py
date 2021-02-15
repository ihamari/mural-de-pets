from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Pet():
    def __init__(self,id,imagem,nome):
        self.id=id
        self.imagem = imagem
        self.nome = nome

lista_pets = [
    Pet(1,'https://olhardigital.com.br/wp-content/uploads/2020/10/20201019024526.jpg','maki'),
    Pet(2,'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg', 'Tobias')
]

class Index(Resource):
    def get(self, nome='Usuário'):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', nome_usuario=nome, lista_pets=lista_pets),200,headers) # no return padrao de um verbo http eh um json o "make_response" do Flask customiza o headers, nesse caso ele faz o browser entender que eh um html

api.add_resource(Index, '/', '/<string:nome>')


if __name__ == '__main__':
    app.run(debug=True) # Para n ser necessario rodar o programa de novo a cada save
