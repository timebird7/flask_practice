from flask import Flask, render_template, send_file, request
from datetime import datetime
import random
app = Flask(__name__)

hogu=[]

@app.route("/")                     # 주문 받는 방법(요청을 받는 방법)
def index():
    return render_template('index.html')           # 서비스 주는 방법(응답을 보내는 방법)

@app.route("/hello/<name>")         # 가변 라우팅
def hello(name):
    return "hello, " + name

@app.route('/rev/<str>')            #뒤집개
def rev(str):
    return str[::-1]

@app.route('/palind/<pal>')         #팰린드롬
def pal(pal):
    return str(pal == pal[::-1])

@app.route('/cube/<num>')           #세제곱
def cube(num):    
    return str(int(num)**3)

@app.route('/isitnewyear')
def hny():
    return 'yes' if datetime.now().month == 1 and datetime.now().day == 1 else 'no'

@app.route('/gh')   # 입력받은 값을 그대로 출력한다.
def gh():
    me = request.args.get('me')
    you = request.args.get('you')
    hogu.append([me, you])
    ran = random.randint(60,100)
    return render_template('gh.html', me = me, you = you, ran = ran)

@app.route('/god')
def god():
    return str(hogu)