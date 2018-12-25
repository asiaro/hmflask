from flask import Flask


app=Flask(__name__)
@app.route('/demo',methods=['GET','POST'])

def index():
    return "DEMO"

if __name__ =='__main__':
    print(app.url_map)
    app.run()



