from flask import Flask, redirect, render_template, request

app = Flask(__name__)

name_cards=[{'cno':1,'name':'spring','tel':'1234'},{'cno':2, 'name':'summer','tel':'2345'}]
cno=3

@app.route("/card/list")
def list():
  error = request.args.get('error')
  message=''
  if error=='insert':
    message= '연락처가 이미 존재합니다'
  elif error == 'delete':
    message = '연락처를 찾을 수 없습니다'
  return render_template("card2/list.html", name_cards=name_cards, message=message)


@app.route("/card/insert", methods=['post'])
def insert():
  global cno
  name=request.form.get('name', None)
  tel= request.form.get('tel', None)
  # 중복이면 에러 처리 (이름과 연락처가 모두 중복이면 에러 코드를 가지고 /card/list로 이동)
  for card in name_cards:  # 모든 명함에 대해서 중복된 명함이 있다면 중지하고 에러코드로 이동하기
    if card['name']==name and card['tel']==tel:
      return redirect("card/list?error=insert")   # 비정상적인 상황
  new_card = {'cno':cno,'name':name,'tel':tel}
  name_cards.append(new_card)
  return redirect("/card/list")       # 정상적인 상황

@app.route("/card/delete", methods=['post'])
def delete():
    cno = int(request.form.get('cno'))
    for card in name_cards:
      if card['cno'] == cno:
        name_cards.remove(card)
        return redirect("/card/list")
    return redirect("/card/list?error=delete")



app.run(debug=True)