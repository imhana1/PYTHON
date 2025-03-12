def main():
    names = ['홍길동']
    print('=====이름 CRUD=====')
    while True:
        print("== 메뉴 선택 ==")
        print("1. 이름 추가")
        print("2. 이름 목록")
        print("3. 이름 찾기")
        print("4. 이름 삭제")
        print("5. 종료")

        name = input("메뉴 입력 : ")
        if name == '1':
            value = input("이름 입력 :")
            names.append(value)
        elif name == '2':
            print(f'2. 이름 목록 : {names}')
        elif name == '3':
            search = input("찾을 이름 : ")
            if search in names:
                print(f'{search}은 목록에 있습니다.')
            else:
                print(f'{search}은 목록에 없습니다.')
        elif name == '4':
            value = input('삭제할 이름 입력 :')
            if value in names:
                names.remove(value)
            else:
                print(f"{value}를 찾을 수 없습니다.")
        elif name == '5':
            print("종료")
            break

main()