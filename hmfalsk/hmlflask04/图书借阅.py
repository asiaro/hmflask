from flask import Flask,render_tempalte,request,flash,redirect,url_for
import base64
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///falsk.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="key"
db=SQLAlchemy(app)

class Author(db.Model):
    __tablename__="authors"
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    books=db.relationship("Book",backref="author")
class Book(db.Model):
    __tablename__="books"
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    books=db.relationship(db.Integer,db.ForeignKey("authors.id"))

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="GET":
        authors=author.query.all()
        return render_template("图书借阅.html",authors=authors)
    author_name=request.form.get("author_name")
    book_name=request.form.get("book_name")
    if not all([author_name,book_name]):
        flash("参数不完整")




@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    pass


@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    pass

if __name__=='__main__':
    db.drop_all()
    db.create_all()

    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)





















