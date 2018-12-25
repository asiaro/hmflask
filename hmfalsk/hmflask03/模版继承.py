from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("demo4_index.html")
@app.route('/detail')
def detail():
    return render_template("demo4_detail.html")
@app.route('/base')
def base():
    return render_template("demo4_base.html")

if __name__ =='__main__':
    app.run(debug=True)

