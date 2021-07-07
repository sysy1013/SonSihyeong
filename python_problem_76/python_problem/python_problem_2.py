
# 함수 이름은 변경 가능합니다.

# menu 1
student_list = []


def Menu1(student):
    student[1] = int(student[1])
    student[2] = int(student[2])
    student_list.append(student)
    print(student_list)


# 학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        # 학생 정보 입력받기
        # 예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        # 예외사항이 아닌 입력인 경우 1번 함수 호출
        try:
            student = input(
                "Enter name mid_score final_score : ").split()
            if student[0] in str(student_list):
                raise NameError

            if student[1].isdigit() == False or student[2].isdigit() == False:
                raise ValueError

            if len(student) > 3:
                raise IndexError

            Menu1(student)
        except IndexError:
            print("Num of data is not 3")
        except ValueError:
            print("Score is no positive integer!")
        except NameError:
            print("Already exist name!")
