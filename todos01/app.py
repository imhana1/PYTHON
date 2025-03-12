from flask import Flask, redirect, session
from todos_view import todos_app

app = Flask(__name__)

# 세션 암호화를 위한 비밀번호 지정
app.config['SECRET_KEY'] = '1234'

app.register_blueprint(todos_app)

# 테스트용 로그인, 로그아웃 함수 -> get 처리
@app.route("/spring")
def test_spring_login() :
    session['username'] = 'spring'
    return redirect("/")

@app.route("/summer")
def test_summer_login() :
    session['username'] = 'summer'
    return redirect("/")

@app.route("/logout")
def test_logout():
    session.clear()
    return redirect("/")

app.run(debug=True)