from flask import Flask,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config.update(
    SECRET_KEY='superna0',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:superna0@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db=SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Poulami!'

@app.route('/new/')
def query_strings(greeting='hello'):
    query_val=request.args.get('greeting',greeting)
    # query_val=request.args['greeting']
    return '<h1> The greeting is : {0} </h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='Poulami'):
    return '<h1>Hello there ! {}</h1>'.format(name)

#string
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1>Here is the string !' + (name) + '</h1>'

#numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> The number you picked is: '+ str(num) +'</h1>'

#add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1,num2):
    return '<h1>The sum is : {}'.format(num1+num2) +'</h1>'

#Floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1,num2):
    return '<h1>The product is : {}'.format(num1*num2) +'</h1>'

#using templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

#jinja templates
@app.route('/watch')
def top_series():
    series_list=['Lucifer',
                 'Friends',
                 'Never have I ever',
                 'Iron fist',
                 'Hundred']
    return render_template('series.html',series=series_list,name="Poulami")

@app.route('/tables')
def series_plus():
    series_dict={'Lucifer':4,
                 'Friends':10,
                 'Never have I ever':7,
                 'Iron fist':4,
                 'Hundred':1}
    return render_template('table_data.html',series=series_dict,name="Poulami")

@app.route('/filters')
def filter_data():
    series_dict={'Lucifer':4,
                 'Friends':10,
                 'Never have I ever':7,
                 'Iron fist':4,
                 'Hundred':1}
    return render_template('filter_data.html',series=series_dict,name=None,series_name='Lucifer')

@app.route('/macros')
def jinja_macros():
    series_dict={'Lucifer':4,
                 'Friends':10,
                 'Never have I ever':7,
                 'Iron fist':4,
                 'Hundred':1}
    return render_template('using_macros.html',series=series_dict)


class Publication(db.Model):
    __tablename__ ='publication'
    
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(80),nullable=False)
    
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Publisher is {}'.format(self.name)
        
class Book(db.Model):
    __tablename__='book'
    
    id=db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String(500),nullable=False,index=True)
    author=db.Column(db.String(350))
    avg_rating=db.Column(db.Float)
    format=db.Column(db.String(50))
    image=db.Column(db.String(100),unique=True)
    num_pages=db.Column(db.Integer)
    pub_date=db.Column(db.DateTime,default=datetime.utcnow())
    
    #Relationship
    pub_id=db.Column(db.Integer,db.ForeignKey('publication.id'))

    def __init__(self,title,author,avg_rating,book_format,image,num_pages,pub_id):
        self.title=title
        self.author=author
        self.avg_rating=avg_rating
        self.format=book_format
        self.image=image
        self.num_pages=num_pages
        self.pub_id=pub_id
    
    def __repr__(self):
        return '{} by {}'.format(self.title,self.author)




if __name__=='__main__':
    db.create_all()
    app.run(debug=True)