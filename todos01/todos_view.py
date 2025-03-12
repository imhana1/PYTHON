# 사용자 입출력하는 함수 : 자바는 Controller, 파이썬은 View
from flask import Blueprint, render_template, redirect, request, session
import datetime as dt

# Blueprint로 현재 뷰 소스의 청사진을 찍어 외부로 내보낸다
# todos_app : 외부로 내보내는 이름
# 'todos_app' : 별칭. 우리는 사용 예정 없음
todos_app = Blueprint('todos_app', __name__)

todos = []
tno = 1

@todos_app.route("/")
def index():
    return render_template("list.html", todos=todos)

@todos_app.route("/write", methods = ['post'])
def write():
    global tno
    # 로그인 안했으면 /로 이동
    login_id = session.get('username')
    if login_id == None : 
        return redirect("/")
    title = request.form.get('title')
    date = dt.datetime.now().strftime('%Y-%m-%d')
    new_todo = {'tno':tno, 'title':title, 'writer':login_id, 'date':date, 'finish':False}
    todos.append(new_todo)
    tno += 1
    return redirect("/")

@todos_app.route("/finish", methods = ['post'])
def finish():
    login_id = session.get('username')
    if login_id == None:
        return redirect("/")
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno'] == tno and todo['writer'] == login_id:
            todo['finish'] = True
    return redirect("/")
    
@todos_app.route("/delete", methods = ['post'])
def delete():
    login_id = session.get('username')
    if login_id == None:
        return redirect("/")
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno'] == tno and todo['writer'] == login_id:
            todos.remove(todo)
    return redirect("/")