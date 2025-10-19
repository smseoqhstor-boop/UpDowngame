com_num = 77
talks = []


while(True):
        try:
            talk= int(input("숫자 입력: "))
            if(len(talks) >4):
                print("5회 이상 시도하셨습니다. 실패!!")
                break
            elif(talk < com_num):
                print("틀렸습니다. 업!!")
            elif(talk > com_num):
                print("틀렸습니다. 다운!!")
            else:
                print("정답!!!")
                break
            talks.append(int(talk))
            print("시도한 숫자는 {} 입니다.".format(talks))
        except:
             print("숫자만 입력해주세요")