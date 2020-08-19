from app import app
from app import manager
from app import db

db.init_app(app)
#db.create_all()

if __name__ == '__main__':
