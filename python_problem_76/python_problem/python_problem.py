num = 0

while True:
    while True:
        try:
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if num >= 4:
                raise TypeError
            break
        except ValueError:
            print("정수를 입력하세요.")
        except TypeError:
            print("1,2,3만 입력해주세요.")

    for i in range(0, num):
        print(f'player A : {i+1}')
