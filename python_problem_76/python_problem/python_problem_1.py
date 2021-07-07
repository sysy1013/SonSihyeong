num = 0
A_count = 0
temp = 0
total = 0
b_count = 0

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
    A_count = num+temp
    total += num

    if total > 31:
        for i in range(temp, 32):
            print(f'player A: {i}')
        print("playerB win!")
        exit()

    for i in range(temp, A_count):
        print(f'player A : {i+1}')
    temp = A_count

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

    b_count = A_count+num
    total += num

    if total > 31:
        for i in range(temp, 32):
            print(f'playerB : {i+1}')
        print("playerA win!")
        exit()

    for i in range(temp, b_count):
        print(f'playerB: {i+1}')
    temp = b_count
3
