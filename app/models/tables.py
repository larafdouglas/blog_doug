from app import db,lm
from datetime import datetime
class Blogpost(db.Model):
    __tablename_='Blogpost'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    categoria = db.Column(db.String(50))
    subcategoria = db.Column(db.String(50))
    username = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime(),default=datetime.utcnow)
    content = db.Column(db.Text())

    def __init__(self,title,categoria,subcategoria,username,date_posted,content):
        self.title = title
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.username = username
        self.date_posted = date_posted
        self.content= content
   

    def __repr__ (self):
        return 'Titulo %r' % self.title
        return 'Subtitulo %r' % self.subtitle
        return 'Autor %r' % self.author
        return 'Data %r' % self.date_posted
        return 'Conteudo %r' % self.content


class Login(db.Model):
    __tablename__='Login'
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True)
    password = db.Column(db.String)

    def __init__(self,username,password):
        self.username=username
        self.password=password
        

    def __repr__ (self):
        return 'Usuario %r' % self.username
        
