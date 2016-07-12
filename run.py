from flask import Flask
from app import app
from app import models

#Create app

if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)
