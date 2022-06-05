from flask import Flask, render_template, send_from_directory, request, url_for, flash, redirect
from turbo_flask import Turbo
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select, text

#______TEST______


#session = Session(engine, future=True)
turbo = Turbo()
db = SQLAlchemy()
login = LoginManager()


#____________BASE DE DATOS___________
class UserModel(UserMixin, db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(80))
	username = db.Column(db.String(100), unique=True)
	password_hash = db.Column(db.String())

	data_for_count = db.relationship('DataModel', backref='data', lazy=True)


	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class DataModel(db.Model):
	__tablename__= 'data'
	id = db.Column(db.Integer, primary_key=True)
	lista_ordenadores = db.Column(db.Integer())
	nombre = db.Column(db.String())
	precio = db.Column(db.Float())
	cantidad = db.Column(db.Float())
	procesador = db.Column(db.String())
	ram = db.Column(db.String())
	disco_duro = db.Column(db.String())
	grafica = db.Column(db.String())

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)

#__________APP_______________
def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '1Retrete!'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/legany/things/programacion/github/repositories/pcweb/website/static/database/pcweb.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	login = LoginManager()
	db.init_app(app)
	turbo.init_app(app)
	login.login_view = 'inicio_sesion'
	login.init_app(app)

	@login.user_loader
	def load_user(id):
		return UserModel.query.get(id)

	@app.before_first_request
	def create_table():
	    db.create_all()

	#_____________Creacion usuarios y inicio de sesión_____________
	def get_user_connection():
		conn = sqlite3.connect('website/static/database/pcweb.db')
		conn.row_factory = sqlite3.Row 
		return conn
	user_connection_db = get_user_connection()
	def register_user():
		conn = get_user_connection()
		data_user = conn.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
		conn.commit()
		conn.close()
	def register_user_exists():
		conn = get_user_connection()
		data_user = conn.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
		conn.commit()
		conn.close()
		return data_user	

	def login_user_internal():
		conn = get_user_connection()
		data_user = conn.execute("SELECT username, password_hash FROM users")
		conn.commit()
		conn.close()


	def primer_ordena(): #Imprime toda la información de la base de datos.
		search = (
			select(DataModel)
			.filter_by(id = 2)
			)
		user_Data = db.session.scalars(search).all()
		return user_Data

	@app.route("/", methods=["GET", "POST"])
	def main():
		return render_template("/main.html", coso="otroCoso")
	@app.route("/", methods=["PUT"])
	def change():
		return render_template("/main.html")
#________________________________________________________________________________________
	@app.route("/basic/mi_primer_pc")
	def basic_mi_primer_pc():
		return render_template("/basic/mi_primer_pc.html",)
	@app.route("/basic/low_cost")
	def basic_low_cost():
		return render_template("/basic/low_cost.html", 
			primer_ordena = primer_ordena(),
			)
	@app.route("/basic/medium")
	def basic_medium():
		return render_template("/basic/medium.html")
	@app.route("/basic/hight_performance")
	def basic_hight():
		return render_template("/basic/hight_performance.html")
	@app.route("/basic/extreme")
	def basic_extreme():
		return render_template("/basic/extreme.html")
#___________________Low cost (Basic)______________________________________________
	@app.route("/basic/low_cost/ryzen3")
	def ryzen3():
		return render_template("/basic/low_cost/ryzen3.html",
			primer_ordena = primer_ordena(),
			)

#____________________________________________________________________________________
	@app.route("/gamer/low_cost")
	def gamer_low():
		return render_template("/gamer/low_cost.html")
	@app.route("/gamer/medium")
	def gamer_medium():
		return render_template("/gamer/medium.html")
	@app.route("/gamer/hight_performance")
	def gamer_hight():
		return render_template("/gamer/hight_performance.html")
	@app.route("/gamer/extreme")
	def gamer_extreme():
		return render_template("/gamer/extreme.html")


	@app.route("/workstation/low_cost")
	def work_low():
		return render_template("/workstation/low_cost.html")
	@app.route("/workstation/medium")
	def work_medium():
		return render_template("/workstation/medium.html")
	@app.route("/workstation/hight_performance")
	def work_hight():
		return render_template("/workstation/hight_performance.html")
	@app.route("/workstation/extreme")
	def work_extreme():
		return render_template("/workstation/extreme.html")


	@app.route("/componentes/procesadores")
	def procesadores():
		return render_template("/componentes/procesadores.html")
	@app.route("/componentes/disco_duro")
	def disco_duro():
		return render_template("/componentes/disco_duro.html")
	@app.route("/componentes/rams")
	def rams():
		return render_template("/componentes/rams.html")
	@app.route("/componentes/tarjeta_grafica")
	def tarjeta_grafica():
		return render_template("/componentes/tarjeta_grafica.html")

	@app.route("/complementos/cables")
	def cables():
		return render_template("/complementos/cables.html")
	@app.route("/complementos/monitores")
	def monitores():
		return render_template("/complementos/monitores.html")
	@app.route("/complementos/raton")
	def raton():
		return render_template("/complementos/raton.html")
	@app.route("/complementos/teclado")
	def teclado():
		return render_template("/complementos/teclado.html")

	return app