from flask import Flask
from flask_restful import Api
from model.pets import PetModel
from resources.index import Index
from resources.pets import PetsResource



app = Flask(__name__)
api = Api(app)


api.add_resource(Index, '/', '/<string:nome>')
api.add_resource(PetsResource,'/pets')

if __name__ == '__main__':
    app.run(debug=True) # Para n ser necessario rodar o programa de novo a cada save
