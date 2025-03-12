# 선생님 풀이

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/add", methods=['get'])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=['post'])
def add_post():
    value1= int(request.form.get('value1'))
    value2= int(request.form.get('value2'))
    hap= value1+value2
    # 새로운 작업으로 보낸다
    return redirect(f"/result?hap={hap}")

@app.route("/result")
def result():
    hap=request.args.get("hap")
    return render_template("result.html", hap=hap)


app.run(debug=True)