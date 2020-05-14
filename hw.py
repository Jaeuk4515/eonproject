n = int(input("작업수를 입력하세요 : "))
m = int(input("작업번호를 입력하세요 : "))

if (0 < n <= 100 and 0 <= m <= n-1):
    rank = list(map(int, input("우선순위를 입력하세요 : ").split()))
    minute = 0
    number = list(range(len(rank)))
    
    while True:
        if rank[0] < max(rank):
            rank.append(rank.pop(0))
            number.append(number.pop(0))
        else:
            minute = minute + 1
            if number[0] == m:
                print(minute, "분")
                break
            else:
                rank.pop(0)
                number.pop(0)

else:
    print("값을 잘못 입력하셨습니다.")
