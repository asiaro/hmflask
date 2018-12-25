from flask import Flask,render_template,session,g,flash
app=Flask(__name__)
app.secret_key="test"


@app.route('/')
def index():
  session["name"]="zs"
  g.age=20
  flash("nh")
  flash("zj")
  return render_template("demo5_var.html")

@app.route('/demo1')
def demo1():
    flash('hh')
    return 'demo1'



if __name__ =='__main__':
    app.run(debug=True)

