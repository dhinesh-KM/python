from Mclass.gradefuncs import *
grades=[]
while True:
    print("--------------------------------------------")
    print("        STUDENT GRADE ANALYZER        ")
    print("--------------------------------------------")
    print("1. ADD STUDENT")
    print("2. ADD GRADE")
    print("3. CALCULATE AVERAGE")
    print("4. CALCULATE CLASS AVERAGE")
    print("5. DISPLAY STUDENT GRADES")
    print("6. Exit")
    
    
    print("choice")
    c=int(input())
    if c==1:
        print("enter the student name:")
        name=str(input())
        add_student(grades, name)
        
    if c==2:
        print("enter the student name to update the grades:")
        name=str(input("enter the name:"))
        grade=[]
        add_grade(grades, name, grade)
        
    if c==3:
        print("enter the student name to calculate the average:")
        name=str(input("enter the name:"))
        calculate_average(grades, name)
        
    if c==4:
        calculate_class_average(grades)
        
    if c==5:
        print("enter the student name to display")
        name=str(input("enter the name:"))
        display_student_grades(grades, name)
        
    elif c==6:
        break
    
   
        
    