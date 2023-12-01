
def add_student(grades, name):
    s=[name]
    grades.append(s)
    
def add_grade(grades, name, grade):
    for sublist in grades:
        if name in sublist:  # name validation
            n=int(input("enter the length of grades:"))
            for i in range(1,n+1):
                a=float(input(f"enter grade{i}:"))  #grade input
                grade.append(a)
            sublist.append(grade)    #append grade list in the sublist
            print(sublist)
            break
    else:
        print("Student name is not found")
        
def  calculate_average(grades, name):
    a=0
    for sublist in grades:
        if name not in sublist:               # name validation
            print("Student name is not found")
            break
            
        n = len(sublist)
        if n > 1:
            n=len(sublist)
            if sublist[0] == name:
                for i in range(n+1):
                    a+=sublist[n-1][i]     #add the grades in sublist["name,[0,1,2]"]
                avg=a/(n+1)
            print(f"Average grade of student {name} is ",avg)
        else:
            print(f"{name}  doesn't have grades,so please add it ")
    
    
def calculate_class_average(grades):
    a = c = avg = 0
    #print(len(grades))
    for sublist in grades:
        n = len(sublist)
        if n > 1:              #length of sublist validation 
            c+=1
            for i in range(n + 1):
                a += sublist[n - 1][i]      #add the grades in sublist["name,[0,1,2]"]
 
            if c<=1:
                avg = a / (n + 1)            
      
            else:
                avg =a / c
    print("the average grade for the entire class",avg)
            
def display_student_grades(grades, name):
    print("---------------------------------------------------------")
    print("                STUDENT GRADE ANALYZER                   ")
    print("---------------------------------------------------------")
    print(grades)
    for sublist in grades:
        a=0
        n=len(sublist)
        if sublist[0] == name:
            print("NAME:",sublist[0])
            for i in range(n+1):
                a+=1
                if n > 1:               #check sublist have grades
                    if a <=n+1:
                        print(f"GRADE {a}: ",sublist[n-1][i])
            print()
            
        