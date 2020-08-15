from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,DateTimeField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class FormBlogpost(FlaskForm):
		id= StringField('id')
		title= StringField('title',validators=[DataRequired()])
		categoria=SelectField('subtitle', choices=[(1,'Estruturas'),(2,'Hidráulica'),(3,'Construção Civil'),(4,'Geotecnia'),(5,'Rodovias')], default=1)
		subcategoria=SelectField('subtitle', choices=[(1,'Estruturas'),(2,'Hidráulica'),(3,'Construção Civil'),(4,'Geotecnia'),(5,'Rodovias')], default=1)
		username=StringField('author')
		date_posted=DateTimeField('date_posted')
		content=TextAreaField('content')

class FormLogin(FlaskForm):
	id=StringField('id')
	username= StringField('username', validators=[DataRequired()])
	password= PasswordField('password', validators=[DataRequired()])
	#remember= BooleanField('remember')