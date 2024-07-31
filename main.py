from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'your_secret_keyskjbfjksbfj_here'  # Set your secret key here

bootstrap = Bootstrap(app)




from flask_app.routes import * # noqa

if __name__ == "__main__":
    app.run(debug=True, port=3000)
