import random

num = 0
A_count = 0
temp = 0
total = 0
b_count = 0


class brGame:

    def __init__(self, playerA, playerB):
        self.playerA = playerA
        self.playerB = playerB

    def playerA(self):
        global num, A_count, temp, total
        try:
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if num >= 4:
                raise TypeError

        except ValueError:
            print("정수를 입력하세요.")
        except TypeError:
            print("1,2,3만 입력해주세요.")
        A_count = num+temp
        total += num

        if total > 31:
            for i in range(temp, 31):
                print(f'playerA: {i+1}')
            print("Computer win!")
            exit()

        for i in range(temp, A_count):
            print(f'playerA : {i+1}')
        temp = A_count

    def Computer(self):
        global num, A_count, b_count, temp, total
        num = 0

        num = random.randint(1, 3)
        b_count = A_count+num
        total += num

        if total > 31:
            for i in range(temp, 31):
                print(f'Computer: {i+1}')
            print("playerA win!")
            exit()

        for i in range(temp, b_count):
            print(f'Computer: {i+1}')
        temp = b_count


brGame("playerA", "Computer")
while True:
    brGame.playerA("playerA")
    brGame.Computer("Computer")
