from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = "t_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.drop_all()
    
    db.create_all()
    admin=User('admin','123@123.com')
    db.session.add(admin)
    db.session.commit()
    
    return 'iii'


if __name__ == "__main__":
    
    app.run(debug=True)


