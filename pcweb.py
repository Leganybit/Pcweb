from website import create_app
from flask_login import LoginManager

app = create_app()

if __name__ == "__main__":
	#(debug=True)
	app.run(debug=True, host="127.0.0.1", port=5004)


