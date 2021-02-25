from flask import Flask, render_template

app = Flask(__name__)

from app import routes
from app import get_weather



if __name__ == "__main__":
	app.run()
