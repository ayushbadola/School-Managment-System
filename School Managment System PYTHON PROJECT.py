import mysql.connector
import random
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE schoolsgrrpublic")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="schoolsgrrpublic")
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE  details1 (name VARCHAR(255), rollnumber VARCHAR(255),adharnumber VARCHAR(255), phonenumber VARCHAR(255), Fathername VARCHAR(255), Mothername VARCHAR(255))")
#mycursor.execute("CREATE TABLE  Marks33 (name VARCHAR(255), rollnumber VARCHAR(255), ENGLISH VARCHAR(255), maths VARCHAR(255), physics VARCHAR(255), Chemistry VARCHAR(255), computerscience VARCHAR(255), totmarks VARCHAR(255), perc VARCHAR(255))")


def detail():
        apr="y"
        while apr=="y":
                N=input("enter your name")
                D=input("enter the Roll number")
                S=input("enter you adhar number")
                P=input("enter phone number")
                R=input("enter Father name")
                F=input("enter Mother name")
                sql = "INSERT INTO  details1 (name, rollnumber, adharnumber, phonenumber, Fathername, Mothername) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (N,D,S,P,R,F)
                mycursor.execute(sql, val)
                mydb.commit()
                J=int(input("enter English marks"))
                mm=int(input("enter Maths marks"))
                B=int(input("enter Physics marks"))
                W=int(input("enter Chemistry marks"))
                H=int(input("enter computer science marks"))
                l=J+mm+B+W+H
                X=str(l)
                h=(J+mm+B+W+H)/5
                Q=str(h)
                sql = "INSERT INTO  Marks33 (name , rollnumber , ENGLISH , maths , physics , Chemistry , computerscience , totmarks , perc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (N,D,J,mm,B,W,H,X,Q)
                mycursor.execute(sql, val)
                mydb.commit()
                print("details has been registered")
                print()
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()



def percentage__():
        apr="y"
        while apr=="y":
                print("press 1 to check specfic student percentage by your choice")
                print("press 2 to check whole class PERCENTAGE")
                print("press 3 for exit")
                c=int(input("enter your choice"))
                if c==1:
                        g=input("enter  Roll number")
                        f="SELECT  name, perc  FROM  Marks33 WHERE  rollnumber=%s"
                        a=(g,)
                        mycursor.execute(f,a)
                        myresult = mycursor.fetchall()
                        for x in myresult:
                                print("name   percentage")
                                print(x)
                elif c==2:
                        mycursor.execute("SELECT  name, perc  FROM  Marks33")
                        myresult = mycursor.fetchall()
                        print("name   percentage")
                        for x in myresult:
                                print(x)
                else:
                        exit()
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()




def topper():
        apr="y"
        while apr=="y":
                mycursor.execute("SELECT max(ENGLISH) FROM Marks33")
                myresult1 = mycursor.fetchall()
                for x in myresult1:
                        print("highest marks in ENGLISH",x)
                        mycursor.execute("SELECT max(maths) FROM  Marks33")
                        myresult2 = mycursor.fetchall()
                for e in myresult2:
                        print("highest marks in MATHS",e)
                        mycursor.execute("SELECT max(physics) FROM  Marks33")
                        myresult3= mycursor.fetchall()
                for r in myresult3:
                        print("highest marks in PHYSICS",r)
                        mycursor.execute("SELECT max(Chemistry) FROM  Marks33")
                        myresult4 = mycursor.fetchall()
                for t in myresult4:
                        print("highest marks in CHEMISTRY",t)
                        mycursor.execute("SELECT max(computerscience) FROM  Marks33")
                        myresult5 = mycursor.fetchall()
                for y in myresult5:
                        print("higest marks in COMPUTER SCIENCE",y)
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()



def failed():
        apr="y"
        while apr=="y":
                print("press 1 for english ")
                print("press 2 for maths")
                print("press 3 for physics")
                print("press 4 for chemistry")
                print("press 5 for computer science")
                d=int(input("enter your choice"))
                if d==1:
                        print("press 1 for passed student in ENGLISH")
                        print("press 2 for failed student in ENGLISH")
                        print("press any key for exit")
                        g=int(input("enter your choice"))
                        if g==1:
                                mycursor.execute("SELECT COUNT(ENGLISH) as count FROM Marks33  WHERE ENGLISH>=33")
                                row=mycursor.fetchone()
                                print("number of student passed in english",row)
                        elif g==2:
                                mycursor.execute("SELECT COUNT(ENGLISH) as count FROM Marks33  WHERE ENGLISH<33")
                                row=mycursor.fetchone()
                                print("number of student failed in english",row)
                        else:
                                exit()
                elif d==2:
                        print("press 1 for passed student in maths")
                        print("press 2 for failed student in maths")
                        print("press any key for exit")
                        g=int(input("enter your choice"))
                        if g==1:
                                mycursor.execute("SELECT COUNT(maths) as count FROM Marks33  WHERE maths>=33")
                                row=mycursor.fetchone()
                                print("number of student passed in maths",row)
                        elif g==2:
                                mycursor.execute("SELECT COUNT(maths) as count FROM Marks33  WHERE maths<33")
                                row=mycursor.fetchone()
                                print("number of student failed in maths",row)
                        else:
                                exit()
                elif d==3:
                        print("press 1 for passed student in PHYSICS")
                        print("press 2 for failed student in PHYSICS")
                        print("press any key for exit")
                        g=int(input("enter your choice"))
                        if g==1:
                                mycursor.execute("SELECT COUNT(physics) as count FROM Marks33 WHERE physics>=33")
                                row=mycursor.fetchone()
                                print("number of student passed in PHYSCIS",row)
                        elif g==2:
                                mycursor.execute("SELECT COUNT(physics) as count FROM Marks33  WHERE physics<33")
                                row=mycursor.fetchone()
                                print("number of student failed in PHYSICS",row)
                        else:
                                exit()
                elif d==4:
                        print("press 1 for passed student in chemistry")
                        print("press 2 for failed student in chemistry")
                        print("press any key for exit")
                        g=int(input("enter your choice"))
                        if g==1:
                                mycursor.execute("SELECT COUNT(Chemistry) as count FROM Marks33  WHERE Chemistry>=33")
                                row=mycursor.fetchone()
                                print("number of student passed in chemistry",row)
                        elif g==2:
                                mycursor.execute("SELECT COUNT(Chemistry) as count FROM Marks33  WHERE Chemistry<33")
                                row=mycursor.fetchone()
                                print("number of student failed in chemistry",row)
                        else:
                                exit()
                elif d==5:
                        print("press 1 for passed student in Computer science")
                        print("press 2 for failed student in Computer science")
                        print("press any key for exit")
                        g=int(input("enter your choice"))
                        if g==1:
                                mycursor.execute("SELECT COUNT(computerscience) as count FROM  Marks33  WHERE computerscience>=33")
                                row=mycursor.fetchone()
                                print("number of student passed in Computer science",row)
                        elif g==2:
                                mycursor.execute("SELECT COUNT(computerscience) as count FROM  Marks33 WHERE computerscience<33")
                                row=mycursor.fetchone()
                                print("number of student failed in Computer science",row)
                        else:
                                exit()
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()



def percentage_pass():
        apr="y"
        while apr=="y":
                print("press 1 for check passed percentage of students")
                print("press 2 for check failed percentage of students")
                p=int(input("enter your choice"))
                mycursor.execute("SELECT COUNT(computerscience) as count FROM Marks33")
                row1=mycursor.fetchone()
                print("total number of student",row1[0])
                if p==1:
                        mycursor.execute("SELECT COUNT(perc) as count FROM Marks33  WHERE perc >=33")
                        row=mycursor.fetchone()
                        pa=row1[0]
                        ap=row[0]
                        i=(ap/pa)*100
                        print("percentage of student passed  ",i)
                elif p==2:
                        mycursor.execute("SELECT COUNT(perc) as count FROM Marks33  WHERE perc<33")
                        row=mycursor.fetchone()
                        pa=row1[0]
                        ap=row[0]
                        i=(ap/pa)*100
                        print("percentage of student  failed",i)
                else:
                        exit()
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()


def above_90():
        apr="y"
        while apr=="y":
                mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc>=90")
                myresult = mycursor.fetchall()
                print()
                print("student geting 90% and above")
                print("name    percentage")
                for x in myresult:
                        print(x)
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()


def percentage_range():
        apr="y"
        while apr=="y":
                print("press 1 student getting 90% and above")
                print("press 2 student getting 80 to less than 90%")
                print("press 3 student getting 70 to less than 80%")
                print("press 4 student getting 60 to less than 70%")
                print("press 5 for student getting 50 less than 60%")
                print("press 6 for student getting less than 50%")
                pr=int(input("enter your choice"))
                if pr==1:
                        mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc>=90")
                        myresult = mycursor.fetchall()
                        print()
                        print("student geting 90% and above")
                        print("name    percentage")
                        for x in myresult:
                                print(x)
                elif pr==2:
                        mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc>=80 and perc<90")
                        myresult = mycursor.fetchall()
                        print()
                        print("student geting 80% to 90%")
                        for x in myresult:
                                print(x)
                elif pr==3:
                        mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc>=70 and perc<80")
                        myresult = mycursor.fetchall()
                        print()
                        print("student geting 70% and above")
                        for x in myresult:
                                print(x)
                elif pr==4:
                        mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc>=60 and perc<70")
                        myresult = mycursor.fetchall()
                        print()
                        print("student geting 70% to 80%")
                        for x in myresult:
                                print(x)
                elif pr==5:
                        mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc>=50 and perc<60")
                        myresult = mycursor.fetchall()
                        print()
                        print("student geting 60% to 70%")
                        for x in myresult:
                                print(x)
                elif pr==6:
                        mycursor.execute("SELECT  name, perc  FROM Marks33 WHERE perc<50")
                        myresult = mycursor.fetchall()
                        print()
                        print("student geting less than 50%")
                        for x in myresult:
                                print(x)
                else:
                        exit()
                apr=input("press y for continue fill the details otherwise press any key for exit the program")
        else:
                exit()



print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------SECONDARY SCHOOL RESULT-------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")
print("   ------------------------------------------------------------------------")



print("1.Press 1 for filling student details and marks")
print("2.Press 2 for check percentage of students")
print("3.Press 3 for check topper subjectwise")
print("4.Press 4 for check number of student pass or fail in specfic")
print("5.Press 5 for check % of student pass in a class")
print("6.Press 6 for check name of student who get 90% and more then 90%")
print("7.Press 7 for check % range wise")
print("PRESS ANY number FOR EXIT ")
bb=int(input("Enter your choice"))


def main():
    if bb==1:
            detail()
    elif bb==2:
            percentage__()
    elif bb==3:
            topper()
    elif bb==4:
            failed()
    elif bb==5:
            percentage_pass()
    elif bb==6:
            above_90()
    elif bb==7:
            percentage_range()
    else:
        exit()
main() 
