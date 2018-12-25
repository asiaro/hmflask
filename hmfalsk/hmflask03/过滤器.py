from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():
   name = "zs"
   height_list = [1,2]
   h1_tag="<h1>标题</h1>"
   html_str=render_template("demo2_filter.html",name=name,
                            height_list=height_list,h1_tag=h1_tag)
   return html_str

def func_list_reverse(s):
    return s[::-1]


app.add_template_filter(func_list_reverse,"li_reverse")







if __name__ =='__main__':
    app.run(debug=True)

