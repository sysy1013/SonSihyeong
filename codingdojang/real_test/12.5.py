# 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.
#health health_regen mana mana_regen#
# 575.6 1.7 338.8 1.63

x = int(input())
y = input()

if (y == 'Cash3000'):
    x -= 3000
else:
    x -= 5000


print(x)
