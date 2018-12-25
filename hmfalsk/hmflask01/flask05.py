from flask import Flask
from flask import Response
from flask import make_response
from flask import request


app=Flask(__name__)
@app.route('/')
def index():
    print(request.cookies.get("isHelp"))
    return "DEMO"


@app.route('/detail')
def detail():
    is_help = request.cookies.get("isHelp")
    if is_help:  # 显示过帮助信息
        return "直接显示漫画"

    # 第一次请求时, 将想要记录的数据设置到响应头的set_cookie字段
    # 创建响应对象
    response = make_response("显示帮助信息")  # type: Response
    # 设置响应头 set_cookie的值只能是str/bytes

    # max-age用于设置过期时间
    response.set_cookie("isHelp", "1", max_age=60*5)

    # 删除cookie  本质是设置max-age=0
    # response.delete_cookie("isHelp")

    return response


if __name__ == '__main__':
    app.run(debug=True)

