from Pokemon import Pokemon

class CRUD_Pokemon:

	#CONSTRUCTOR
	def __init__(self):

		self.pokemon = []
		self.contador = 0


	#METODO CREAR POKEMON
	def crear(self,nombre,especie,tipo,foto):

		for poke in self.pokemon:

			if poke.nombre == nombre:
				print(' el nombre ya esta en uso')
				return False

		nuevo = Pokemon(self.contador,nombre,especie,tipo,foto)		
		self.pokemon.append(nuevo)	
		self.contador += 1
		return True

	def listar(self):
	
		print('id:\tNombre:\t\tNombre de usuario:')

		for poke in self.pokemon:

			print(str(poke.id) + '\t' + poke.especie + '\t\t' + poke.nombre)	

var_crud = CRUD_Pokemon()

var_crud.crear('Pika','Pikachu','Electrico','https://www.google.com/url?sa=i&url=https%3A','pas1223')
var_crud.crear('Chari','Charizard','Fuego','https://www.google.com/url?sa=i&url=https%3A','pass123')

var_crud.listar()
