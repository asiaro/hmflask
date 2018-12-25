from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:mysql@127.0.0.1:3306/test22"

app.config["SQLALCHENY_TRACK_MODIFCATIONS"]=False
app.config["SQLALCHEMY_ECHO"]=True


db=SQLAlchemy(app)

class User(db.Model):
    __tablename__="t_user"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),unique=True,nullable=False)
    @app.route('/')
    def index():
        db.drop_all()
        db.create_all()
        return "index"


    if __name__=='__main_':
        app.run(debug=True)




