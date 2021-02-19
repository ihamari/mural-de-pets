from flask_restful import Resource, reqparse
from model.pets import lista_pets, PetModel
from flask import make_response, request

parser = reqparse.RequestParser() # reqparse é uma biblioteca que contém RequestParser, Argument. O RequestParser é uma classe que serve para validar os argumentos do objeto criado
parser.add_argument('imagem', type=str)
parser.add_argument('nome',type=str, required=True)


class PetsResource(Resource):
    def get(self,id=None):
        if id==None :
            lista_pets_dict = []
            for pet in lista_pets:
                lista_pets_dict.append(pet.serialize())
                
            return lista_pets_dict, 200

        else:
            for i,pet in enumerate(lista_pets): 
                if pet.id == id :
                    petizinho = i
                    break
                
            return lista_pets[petizinho].serialize(),200


    def post(self):
        args = parser.parse_args()# parse_args verifica os parâmetros da requisição a partir do parser
        if len(lista_pets) == 0 :
            id = 1
        else :
            id = lista_pets[-1].id + 1

        lista_pets.append(PetModel(id,args['imagem'],args['nome']))

        return {'mesagem': 'item criado' },201
        

    def put(self, id = None):
        args = parser.parse_args()
        for pet in lista_pets:
            if pet.id == id:
                pet.nome = args['nome']
                pet.imagem =args['imagem']

        return {'mesagem': 'item editado' },200


    def delete(self, id = None):
        for i,pet in enumerate(lista_pets): #loopa o indice(i) junto com o item
            if pet.id == id :
                deletar = i
                break
        
        lista_pets.pop(deletar)
        return {'mesagem' : 'item deletado'},200


