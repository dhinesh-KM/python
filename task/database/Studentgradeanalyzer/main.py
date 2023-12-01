import database as db
from Mclass.gradefuncs import Student
from pymongo import MongoClient 
  
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
    

s= Student()
while True:
    print("--------------------------------------------")
    print("        STUDENT GRADE ANALYZER        ")
    print("--------------------------------------------")
    print("1. ADD STUDENT")
    print("2. ADD GRADE")
    print("3. CALCULATE AVERAGE")
    print("4. CALCULATE CLASS AVERAGE")
    print("5. DISPLAY STUDENT GRADES")
    print("6. DISPLAY ALL ")
    print("7. DELETE STUDENT")
    print("8. EXIT")
    
    print("Enter the choice:")
    try:
        c=int(input())
        if c==1:
            name = input("enter the student name: ")
            student_data = {"name" : name }
            s.add_student( student_data )
        
        elif c==2:
            name=str(input("enter the student name to update the grades: "))
            if db.mycol.count_documents({"name": name}) > 0:
                s.add_mark(name)
            else:
                print(f"{name} doesn't found so please add the name")
           
        elif c==3:
            name=str(input("enter the student name to display the average: "))
            s.display_average(name)
        
        elif c==4:
            s.display_total_average()
        
        elif c==5:
            print("enter the student name to display student grades: ")
            name=str(input())
            s.display_student(name)
        
        elif c==6:
            s.display_all()
        
        elif c==7:
            name = str(input("enter the student name to delete the document: "))
            s.delete_student(name)
        
        elif c==8:
            break
        
        else:
            print("INCORRECT CHOICE")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    

    
        
        
    