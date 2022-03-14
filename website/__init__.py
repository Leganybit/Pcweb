from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def main():
		return render_template("/main.html")
#________________________________________________________________________________________
	@app.route("/basic/mi_primer_pc")
	def basic_mi_primer_pc():
		return render_template("/basic/mi_primer_pc.html")
	@app.route("/basic/low_cost")
	def basic_low_cost():
		return render_template("/basic/low_cost.html")
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
		return render_template("/basic/low_cost/ryzen3.html")

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