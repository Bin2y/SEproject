from os import major
from unicodedata import name


class student:
    def __init__():
        self.name = name
        self.studentNumber = studentNumber
        self.major = major
        
    def registClass() #강의 신청
    def searchClass() #강의 검색
    def editClass()   #강의 정정
    def deleteClass() #강의 삭제
    def readBasket() #장바구니 열람
    def readSchedule() #시간표 열람
    

class university:
    def checkStudents(); #학생수, 학생 정보확인
    def makeClass()      #강의 개설
    def removeClass()    #강의 폐쇄
    

class basket:
    def putClass() #강의 담기
    def cancleClass() #강의 빼기
    def changeClass() #우선순위 변경
    

def main():
    print("course registration 2.0 System\n")
    print("---Login---")
    stNum = int(input("Student Number : "))
    print("---Login Success---\n")
    print("course registration 2.0 System\n")
    print("1. View your Class Schedule")
    print("2. View Classes and Regist, Cancel")
    print("3. View your Basket")
    print("4. Change Basket's Priority")
    num = int(input("Select Option : "))
    print("-----------------------")
    print("|No.|    Type   |Grade|   class Name   |학점|Professor |   class time    |")
    print("| 1 |  major    |  2  | Data Structure | 3  |Professor |   Fri 7 8 9()   |")
    print("| 2 |  GE class |  -  |Japanese writing| 2  |Professor |   Mon 1   2()   |")
    print("| 3 |  major    |  3  | SW Engineering | 3  |Professor |   Tue 7 8 9()   |")
    print("| 4 |  GE class |  -  | Data Structure | 2  |Professor |   Fri 3 4 5()   |")
    print("| 5 |  major    |  -  |System Operation| 3  |Professor | Tue 3 Thu 1 2() |")
    
    a = int(input("Enter the number of the class you want to change : "))
    b = int(input("NO."+str(a)+" selected, What number do you want to change with? :"))
    print("NO."+str(a)+" and NO."+str(b)+" changed successfully!!")
    print("-----------------------")
    print("|No.|    Type   |Grade|   class Name   |학점|Professor |   class time    |")
    print("| 1 |  major    |  3  | SW Engineering | 3  |Professor |   Tue 7 8 9()   |")
    print("| 2 |  GE class |  -  |Japanese writing| 2  |Professor |   Mon 1   2()   |")
    print("| 3 |  major    |  2  | Data Structure | 3  |Professor |   Fri 7 8 9()   |")
    print("| 4 |  GE class |  -  | Data Structure | 2  |Professor |   Fri 3 4 5()   |")
    print("| 5 |  major    |  -  |System Operation| 3  |Professor | Tue 3 Thu 1 2() |")
    
    #include <iostream>
    #include <algorithm>
    
    

main()
