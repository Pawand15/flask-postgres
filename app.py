import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
os.environ['DATABASE_URI'] = "postgresql://postgres:postgres@10.38.6.42:5432/ntnx"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)

from model import User


@app.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
