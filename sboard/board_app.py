from flask import Flask, render_template, request, redirect
import datetime as dt

app = Flask(__name__)

# 목록: get(∵변경하지 않으니까)
# 작성: get, post(∵화면을 보여주고 변경하니까)
# 읽기: get
# 변경: post(∵왜 post만? 읽기에서 처리할거라서)
# 삭제: post(∵왜 post만? 읽기에서 처리할거라서)

boards = []
bno = 1

# 목록
@app.route('/')
def board_list():
    return render_template('list.html', boards = boards)
    pass

# 작성
@app.route('/write', methods = ['get', 'post'])
def board_write():
    global bno  # bno 여기서 해도 되긴 해
    if request.method == 'GET':
        return render_template('write.html')
    elif request.method == 'POST':
        # 글쓴이, 제목, 내용, 날짜, 조회수
        writer = request.form.get('writer')
        title = request.form.get('title')
        content = request.form.get('content')
        date = dt.datetime.now().strftime('%Y-%m-%d')
        new_board = {'bno':bno, 'title':title, 'writer':writer, 'content':content, 'date':date, 'read_cnt':0}
        boards.append(new_board)
        bno += 1
        return redirect(f'/read?bno={new_board['bno']}')  # bno값 가져와야해서 f문자열 사용했어

# 읽기
@app.route('/read')
def board_read():
    bno = int(request.args.get('bno'))
    for board in boards:
        if board.get('bno') == bno:  # board.get으로 bno 꺼낸거야~ board['bno']랑 목적은 같아
            board['read_cnt'] = board['read_cnt']+1
            return render_template('read.html', board = board)
        # 이 위치는 else위치 / else가 의미하는게 bno 일치하는거를 못찾은거야? 아님! 못찾았는지는 for문을 벗어나야 알 수 있음
    # 못찾은 경우는 여기
    return redirect('/')

# 변경
@app.route('/update', methods = ['POST'])
def board_update():
    # 보통 사용자가 입력한 값을 바꾸는게 업데이트
    # 글번호, 글쓴이, 제목, 내용, 작성일, 조회수
    # 찾아서 바꿔야해 -> 그 기준이 글번호(! 글번호는 값이 변경되어도 안되고 값이 겹쳐도 안됨!)
    bno = int(request.form.get('bno'))
    title = request.form.get('title')
    content = request.form.get('content')
    for board in boards:
        if board.get('bno') == bno:
            board['title'] = title
            board['content'] = content
            return redirect(f'/read?bno={bno}')  # for문 안에서 bno 찾으면 for문 벗어나지 못하니까 return 하고 강제종료
    return redirect('/')
    

# 삭제
@app.route('/delete', methods = ['POST'])
def board_delete():
    bno = int(request.form.get('bno'))
    for board in boards:
        if board.get('bno') == bno:
            boards.remove(board)
            break  # for문 안끝나네? 여기 break 걸어도 되고 그냥 return 걸어도 ㅇㅋ 근데 break 거는게 더 낫긴 해. 동작하는거랑 관계x긴 한데 for문 끝내주자
    return redirect('/')



app.run(debug=True)