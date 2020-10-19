from flask import Flask
from Usuario import Usuario

misUsuario = []
misUsuario.append(Usuario(1,'user','123'))
misUsuario.append(Usuario(2,'user2','123'))


app = Flask(__name__)

@app.route("/")
def index():
	nombre = misUsuario[0].usuario
	return "<h1>Si Sale el Lab</h1>"

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)	