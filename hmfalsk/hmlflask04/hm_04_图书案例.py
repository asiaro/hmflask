from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置数据库连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///falsk.db"
# 是否设置追踪数据库修改(会占用一定的内存,不建议开启)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "test"

# 创建数据库连接对象
db = SQLAlchemy(app)


# 作者模型  一
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义关系属性
    books = db.relationship("Book", backref="author")


# 书籍模型  多
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 1.在多的一方定义外键
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        # 从数据库中取出真实的数据
        authors = Author.query.all()  # type: list[Author]
        # 将数据进行模板渲染
        return render_template("图书借阅.html", authors=authors)

    # POST
    # 获取数据
    author_name = request.form.get("author_name")
    book_name = request.form.get("book_name")
    # 校验数据  all([]) 如果列表元素都有值(不是0 / None / 空字符串),则返回True
    if not all([author_name, book_name]):
        flash("参数不完整")
        return redirect(url_for("index"))

    # 先判断是否有该作者
    try:
        author = Author.query.filter_by(name=author_name).first()
    except BaseException as e:
        flash("数据库查询失败: %s" % e)
        return redirect(url_for("index"))

    # 判断是否已经有该书籍
    book = Book.query.filter_by(name=book_name).first()
    if book:
        # 如果有, 则提示: 该书籍已存在
        flash("该书籍已存在")
        return redirect(url_for("index"))

    if author:
        # 如果没有该书籍, 则添加新书籍, 并且关联该作者
        new_book = Book(name=book_name)
        author.books.append(new_book)  # 关联数据
        try:
            db.session.add(new_book)
            db.session.commit()
        except BaseException as e:
            db.session.rollback()  # 回滚
            flash("数据库查询失败: %s" % e)
            return redirect(url_for("index"))
    else:
        # 没有该作者, 则添加新书籍和新作者, 并且关联数据
        new_book = Book(name=book_name)
        new_author = Author(name=author_name)
        new_author.books.append(new_book)  # 关联数据
        db.session.add_all([new_book, new_author])
        db.session.commit()

    return redirect(url_for("index"))


# 删除作者
@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    # 根据前端发过来的作者信息, 来查询对应的作者模型
    author = Author.query.get(author_id)
    # 从数据库中删除该作者和其所有的书籍
    # 一对多关系中, 先删除多的一方, 再删除一的一方
    Book.query.filter_by(author_id=author.id).delete()
    db.session.delete(author)
    db.session.commit()

    return redirect(url_for("index"))


@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    # 查询书籍模型
    book = Book.query.get(book_id)
    # 删除书籍模型
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
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

    app.run(port=9000, debug=True)
