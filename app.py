#imports the flask class from flask module
from flask import Flask

#creates the application object
app = Flask(__name__)

#use decorators to link the function url
@app.route('/')
def home():
	return 'hello world!'

if __name__ == "__main__":
	app.run(debug=True)

