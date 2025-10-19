import random as r
com_num = r.randrange(1,101)
user_coin = 100

def updownGame(com_num,user_num):
    if(user_num > com_num):
        print("<컴> : 다운!")
    elif(user_num < com_num):
        print("<컴> : 업!")
    else:
        return True

while(user_coin >0):
    print("현재 coin : {}".format(user_coin))
    bet_coin = int(input("배팅할 금액: "))
    print("현재 배팅된 총 coin: ")

    while(bet_coin > user_coin):
        print("당신이 가지고 있는 코인은 {} 입니다. 다시 입력해라잇!".format(user_coin))
        bet_coin = int(input("배팅할 금액: "))

    life = 10
    while(life >0):
        print("현재 남은 기회 : {}".format(life))
        try:
            user_num = int(input("숫자입력: "))

            if(user_num > 100):
                print("100이하 숫자만 입력해주세요~")
                continue

            if updownGame(com_num,user_num):
                print("정답 맞추셨습니다.")
                break

            life -= 1

        except ValueError:
            print("제대로 된 숫자를 입력해주세요!")
    
    if(life > 0):
        #게임 승리
        user_coin = user_coin + bet_coin
    else:
        #게임 패배
        user_coin = user_coin - bet_coin

print("코인을 다 잃으셨습니다.ㅠㅠ")
