from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, make_response, redirect
from flask.json import jsonify
from CoinInfo import CoinInfo
import jwt
from summarizer import Summarizer

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Aleke03072003@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin_name =  db.Column(db.String)
    title = db.Column(db.String)
    body = db.Column(db.String)
    link =  db.Column(db.String)

    def __init__(self, coin_name, title, body, link):
        self.coin_name = coin_name
        self.title = title
        self.body = body
        self.link = link

    def __repr__(self):
        return '<Title %r>' % self.title


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(200), unique=True, nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
                
        if request.form['password'] == '' or request.form['username'] == '':
            error = ["empty"]
            return render_template("login.html", error = error)

        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username= username).first()

        if user:
            if user.password == password:
                token = jwt.encode({'user':username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
                user.token = token
                db.session.add(user)
                db.session.commit()
                url = "/protected?token=" + token
                return redirect(url)
            else:
                error = ['password']
                return render_template("login.html", error=error)
        else:
            error = ["username"]
            return render_template("login.html", error = error)

    elif request.method == 'GET':
        return render_template('login.html')


@app.route("/sign_up", methods = ['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        error=[]
        if request.form['password1'] == '' or request.form['password2'] == '' or request.form['username'] == '':
            error.append("empty")

        if Users.query.filter_by(username = request.form['username']).first():
            error.append("exists")

        if (request.form['password1'] != request.form['password2']):
            error.append("different")

        if len(error) != 0:
            print (error)
            return render_template("reg.html", error = error)
        
        username = request.form['username']
        password = request.form['password1']
        token = jwt.encode({'user':username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])

        user = Users(username, password)
        user.token = token
        db.session.add(user)
        db.session.commit()
        url = "/protected?token=" + token
        return redirect(url)

    elif request.method == 'GET':
        return render_template('reg.html')


@app.route("/protected", methods = ['POST', 'GET'])
def protected():
    token = request.args.get('token')
    db_token = Users.query.filter_by(token=token).first()
    if (not db_token):
        #return make_response("<h1>Hello, could not verify the token</h1>")
        return redirect(url_for("login"))

    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"] )
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login"))

    
        
    if request.method == 'POST':
        coin_name = request.form['coin'].lower()

        db_articles = News.query.filter_by(coin_name = coin_name).all()

        if (db_articles):
            return render_template('protected.html', articles = db_articles)

        coininfo = CoinInfo()
        articles = coininfo.get_paragraphs(coin_name)
        summarizer = Summarizer()
        for article in articles:
            article['body'] = summarizer.summarize(article['link'])
            db.session.add(News(coin_name, article['title'], article['body'], article['link']))
        
        db.session.commit()

        return render_template('protected.html', articles = articles)
       
    elif request.method == 'GET':
        return render_template('protected.html')


if __name__ == '__main__':
    app.run(debug=True)