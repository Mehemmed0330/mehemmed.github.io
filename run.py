from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

from models import *


migrate = Migrate(app, db)



# app routes
from app.routes import *

# admin routes
from admin.routes import *
if __name__ == '__main__':
    app.run(debug=True)


