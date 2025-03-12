from flask import Flask, render_template, request
app = Flask(__name__)


# 숫자 입력화면
@app.route("/start")
def start():
    return render_template("start2.html")

# 입력한 값을 출력
@app.route("/end")
def end():
    value1 = int(request.args.get("value1"))
    value2 = int(request.args.get("value2"))
    result = value1 + value2
    return render_template("end2.html", result = result)

app.run(debug=True)