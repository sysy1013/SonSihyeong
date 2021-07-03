korean, english, mathematics, science = map(int, input().split())
if(korean < 0 or korean > 100 or english < 0 or english > 100 or mathematics < 0 or mathematics > 100 or science < 0 or science > 100):
    print("잘못된 점수")
else:
    avg = (korean+english+mathematics+science)/4
    if(avg > 80):
        print("합격")
    else:
        print("불합격")
