
class Usuario:

	def __init__(self, id, usuario, passw):

		self.id = id
		self.usuario = usuario
		self.passw = passw

	def auntenticar(self, usuario, passw):

		if self.usuario == usuario and self.passw == passw:

			print("La auntenticación fue correcta")
			return True

		print("La autenticacion fue incorrecta")
		return False
					