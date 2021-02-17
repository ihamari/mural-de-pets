class PetModel():
    def __init__(self,id,imagem,nome):
        self.id=id
        self.imagem = imagem
        self.nome = nome

    def serialize(self):
        return {
            "id": self.id,
            "imagem" : self.imagem,
            "nome" : self.nome
        }


lista_pets = [
    PetModel(1,'https://olhardigital.com.br/wp-content/uploads/2020/10/20201019024526.jpg','maki'),
    PetModel(2,'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg', 'Tobias')
]

