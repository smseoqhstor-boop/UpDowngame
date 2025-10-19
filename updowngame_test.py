com_num = 77
life = 5

def updownGame(com_num,user_num):
    if(user_num > com_num):
        print("<컴> : 다운!")
    elif(user_num < com_num):
        print("<컴> : 업!")
    else:
        return True

while(life > 0):
    print("현재 life : {}".format(life))

    try:
        user_num = int(input("숫자입력: "))

        if updownGame(com_num,user_num):
            print("정답 맞추셨습니다.")
            exit()

        life = life - 1

    except ValueError:
        print("제대로 된 숫자를 입력해주세요!")
    

print("기회를 다 잃으셨습니다.ㅠㅠ")