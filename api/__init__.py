from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Nowe DB
# host = "lucky.db.elephantsql.com",
# database = "boaflhol",
# user = "boaflhol",
# password = "W0uDCKGtsASbQSjYDCMs-h1o-lxqdE4n"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://mzhvipvp:LKFCU5m3TA53AkdQf0l3EbO4ww8Dw-Ex@snuffleupagus.db.elephantsql.com/mzhvipvp:5432/mzhvipvp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API SDasdasda!!'
