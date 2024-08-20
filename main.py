from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Set your secret key here
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)


bootstrap = Bootstrap(app)




from flask_app.routes import * # noqa
from database import * # noqa

if __name__ == "__main__":
    app.run(debug=True, port=3000)
