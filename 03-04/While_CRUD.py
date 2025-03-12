# 숫자 리스트를 만드로 CRUD하는 예제
# 1:숫자 추가, 2:숫자리스트, 3:숫자평균, 4:숫자삭제, 5:종료

def main():
    nums = [75]
    print("####숫자 CRUD 프로그램 ####")
    while True:
        print("== 메뉴 선택 ==")
        print("1. 숫자 추가")
        print("2. 숫자 목록")
        print("3. 숫자 평균")
        print("4. 숫자 삭제")
        print("5. 종료")

        choice = input("메뉴 입력 :")
        if choice == '1':
            value = int(input("숫자 입력 :"))
            nums.append(value)
        elif choice == '2':
            print(f"2. 숫자 목록 : {nums}")
        elif choice == '3':
            average = sum(nums)/len(nums)
            print(f"3. 숫자 평균 : {average}")
        elif choice == '4':
            value = int(input("삭제할 숫자 입력 :"))
            if value in nums:
                nums.remove(value)
            else:
                print(f"{value}를 찾을 수 없습니다")
        elif choice == '5':
            print("종료")
            break

main()

