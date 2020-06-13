from flask import Flask, render_template,request, redirect
import json
from flask_sqlalchemy import SQLAlchemy

with open("config.json",'r') as c:
    params=json.load(c)['params']

app = Flask(__name__)
db = SQLAlchemy(app)
class Posts(db.Model):

    '''Posts database attributes..
        sno,Fname,lname
    '''

    sno = db.Column(db.Integer, primary_key=True)
    Fname = db.Column(db.String(10), unique=False, nullable=False)
    Lname = db.Column(db.String(10), unique=False, nullable=False)

local_server = True

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

@app.route('/', methods=['GET','POST'])
def display():
    posts = Posts.query.all()
    return render_template('index.html',params=params,posts=posts)



@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method == "POST":
        Fname = request.form.get('Fname')
        Lname = request.form.get('Lname')

        post = Posts.query.filter_by(sno=sno).first()
        post.Fname = Fname
        post.Lname = Lname
        db.session.commit()
        return redirect('/update/' + str(sno))

    post = Posts.query.filter_by(sno=sno).first()
    return render_template("update.html", params=params, post=post, sno=sno)


@app.route("/delete/<int:sno>", methods=['GET','POST'])
def delete(sno):
    post = Posts.query.filter_by(sno=sno).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)