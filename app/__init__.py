from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

from flask.views import MethodView

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate=Migrate(app,db)
manager=Manager(app)
Breadcrumbs(app=app)
bp = Blueprint('bp', __name__,)

manager.add_command('db', MigrateCommand)

lm = LoginManager(app)
@lm.user_loader
def load_user(user_id):
    return None

from app.models import tables, forms
from app.controllers import default