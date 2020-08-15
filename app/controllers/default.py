from app import app,db, lm, bp
from flask import render_template, flash, redirect, url_for
from app.models.tables import Blogpost, Login
from app.models.forms import FormBlogpost, FormLogin
from datetime import datetime
from flask_login import login_user





@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)


@app.route('/add',methods=["GET","POST"])
def add():
    form = FormBlogpost()

    if form.validate_on_submit():
        title=form.title.data
        categoria=form.categoria.data
        subcategoria=form.subcategoria.data
        username=form.username.data
        content=form.content.data

        post = Blogpost(title=title,categoria=categoria, subcategoria=subcategoria, username=username, content=content, date_posted=datetime.now())
        db.session.add(post)
        db.session.commit()

    return render_template('add.html',form = form)


@app.route('/login',methods=['GET','POST'])

def login():
    form2= FormLogin()
    if form2.validate_on_submit():

        u=Login.query.filter_by(username=form2.username.data).first()

        if u and u.password == form2.password.data:
            login_user(u)
            flash('Logged In')
            return redirect(url_for('index'))
            
        else:
            flash('Invalid Login')

    return render_template('login.html', form2=form2)


@lm.user_loader
def load_user(id):
    return Login.query.filter_by(id=id).first()

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('index.html'))
    

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)



#@app.route('/<categoria>')
#def categoria(categoria):
    #posts = Blogpost.query.filter(Blogpost.categoria==categoria).all()
    #for post in posts:
    #return 'Hello %s' % posts



@app.route('/<categoria>/<subcategoria>')
@app.route('/<categoria>')
def subcategoria(categoria,**kwargs):
    
    posts = Blogpost.query.filter(Blogpost.categoria==categoria).all()
    for post in posts:
        return 'Hello %s' % posts
    subcategoria=kwargs.get('subcategoria')
    postssub=Blogpost.query.filter(Blogpost.subcategoria==subcategoria).all()
    for post in postssub:
        return 'Hello %s ' % postssub












'''@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))'''