class Pokemon:

	def __init__(self,id,nombre,especie,tipo,foto):
		self.id = id
		self.nombre = nombre
		self.especie = especie
		self.tipo = tipo
		self.foto = foto
		self.passw = passw

	def imprimir_tipo(self):
		print(self.nombre);



#pikachu = Pokemon(2,'Pika','Pikachu','Electrico','https://www.google.com/url?sa=i&url=https%3A','pas1223')
#pikachu.imprimir_tipo()

#charizard = Pokemon(2,'Chari','Charizard','Fuego','https://www.google.com/url?sa=i&url=https%3A','pass123')
#charizard.imprimir_tipo()

#pikachu.autenticar('Pika','pass123')
