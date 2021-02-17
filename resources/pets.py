from flask_restful import Resource, reqparse
from model.pets import lista_pets, PetModel
from flask import make_response, request

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('imagem', type=str)
parser.add_argument('nome',type=str, required=True)

class PetsResource(Resource):
    def get(self):
        lista_pets_dict = []
        for pet in lista_pets:
            lista_pets_dict.append(pet.serialize())

        return lista_pets_dict, 200


    def post(self):
        args = parser.parse_args()# parse_args verifica os parâmetros da requisição a partir do parser
        lista_pets.append(PetModel(args['id'],args['imagem'],args['nome']))
        return {'mesagem': 'item criado' },201
        


    def put(self):
        print('executando put')


    def delete(self):
        print('executando delete')


