# 딕셔너리 버전...

# menu 1
from typing import Type


student = {}

# def findStudentByName(studentName: str) -> bool:
#   for student in student_list:
#       if student[0] == studentName:
#          return True
#   return False


def Menu1(name, mid, final):
    try:
        student[name] = [mid, final]
    except:
        print("Number of data is not 3!")


# menu 2


def Menu2():
    # 학점 부여 하는 코딩
    for key in student:
        if len(student) < 4:
            avg = (int(student[key][0]+student[key][1]))/2
            if 100 >= avg >= 90:
                student[key] = [student[key][0], student[key][1], 'A']
            elif avg >= 80:
                student[key] = [student[key][0], student[key][1], 'B']
            elif avg >= 70:
                student[key] = [student[key][0], student[key][1], 'C']
            else:
                student[key] = [student[key][0], student[key][1], 'D']


def Menu3():
    # 출력 코딩
    print('-------------------------')
    print('name\tmid\tfinal\tgrade')
    print('-------------------------')
    for i in student:
        print(
            f'{i}\t{student[i][0]}\t {student[i][1]}\t{student[i][2]}')


def Menu4(del_s):
    # 학생 정보 삭제하는 코딩
    del student[del_s]
    print(f'{del_s} student information is deleted.')


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
            name, mid, final = input(
                "Enter name mid_score final_score : ").split()
            if name in student:
                raise NameError

            if mid.isdigit() == False or final.isdigit() == False:
                raise ValueError

            Menu1(name, mid, final)
        except IndexError:
            print("Num of data is not 3")
        except ValueError:
            print("Score is no positive integer!")
        except NameError:
            print("Already exist name!")

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력
        try:
            Menu2()

            if len(student) == 0:
                raise ValueError
            if len(student) > 0:
                raise IndexError
        except IndexError:
            print("Grading to all students.")
        except ValueError:
            print("No student Data!")

    elif choice == "3":
        # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        # 예외사항이 아닌 경우 3번 함수 호출
        try:
            if len(student) == 0:
                raise ValueError
            for i in list(student.values()):
                if len(i) != 3:
                    raise IndexError
                else:
                    continue
            Menu3()
        except ValueError:
            print("No student Data!")
        except IndexError:
            print("There is a student who did't get grade")

    elif choice == "4":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is
        try:
            if len(student) == 0:
                raise IndexError

            del_student = input("Enter the name to delete ")

            if del_student in student:
                Menu4(del_student)
            else:
                raise TypeError

        except TypeError:
            print("Not exist name")
        except IndexError:
            print("No student Data!")
    elif choice == "5":
        # 프로그램 종료 메세지 출력
        # 반복문 종료
        print("Exit Program!")
        exit()

    else:
        print("Wrong number. Choose again")


# 리스트는 시간이 남아서.. 평가는 위에 코드로 해주십시오....ㅠ
# menu 1
"""from typing import Type


student_list = []


def findStudentByName(studentName: str) -> bool:
    for student in student_list:
        if student[0] == studentName:
            return False
    return True


def Menu1(student):
    student[1] = int(student[1])
    student[2] = int(student[2])
    student_list.append(student)

# menu 2


def Menu2():
    # 학점 부여 하는 코딩
    for i in range(len(student_list)):
        if len(student_list) < 4:
            avg = (student_list[i][1]+student_list[i][2])/2
            if 100 >= avg >= 90:
                student_list[i].append("A")
            elif avg >= 80:
                student_list[i].append("B")
            elif avg >= 70:
                student_list[i].append("C")
            else:
                student_list[i].append("D")


def Menu3():
    # 출력 코딩
    print('-------------------------')
    print('name\tmid\tfinal\tgrade')
    print('-------------------------')
    for i in range(len(student_list)):
        print(
            f'{student_list[i][0]}\t{student_list[i][1]}\t {student_list[i][2]}\t{student_list[i][3]}')


def Menu4(del_s):
    # 학생 정보 삭제하는 코딩
    for i in range(len(student_list)):
        if student_list[i][0] == del_s:
            del student_list[i]
            # print("here4")
    print(f'{del_s} student information is deleted.')


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

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력
        try:
            Menu2()

            if len(student_list) < 4:
                raise IndexError

        except IndexError:
            print("Grading to all students.")
        except ValueError:
            print("No student Data!")

    elif choice == "3":
        # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        # 예외사항이 아닌 경우 3번 함수 호출
        try:
            Menu3()

            if len(student_list) == 0:
                ValueError
            if len(student_list) < 4:
                IndexError

        except ValueError:
            print("No student Data!")
        except IndexError:
            print("There is a student who did't get grade")

    elif choice == "4":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is
        try:
            # print("len: ", student_list[0], len(student_list[0]))
            if len(student_list) == 0:
                raise IndexError
            else:
                del_student = input("Enter the name to delete :")
                # print("del_student: ", del_student)
                if findStudentByName(del_student):
                    raise TypeError
                else:
                    # print("here2")
                    Menu4(del_student)
        except TypeError:
            print("Not exist name")
        except IndexError:
            print("No student Data!")
    elif choice == "5":
        # 프로그램 종료 메세지 출력
        # 반복문 종료
        print("Exit Program!")
        exit()

    else:
        print("Wrong number. Choose again")"""
