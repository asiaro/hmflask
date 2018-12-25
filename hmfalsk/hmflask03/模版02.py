from flask import Flask,render_template
app=Flask(__name__)


class User:
    type="vip"
    def is_login(self):
        return True

@app.route('/')
def index():
    name="zs"
    age_dict={"mane":"zs","age":20}
    height_list=[1,2]

    user=User()
    return render_template("demo.html", name=name, age_dict=age_dict, height_list=height_list, user=user)

if __name__ =='__main__':
    app.run(debug=True)

