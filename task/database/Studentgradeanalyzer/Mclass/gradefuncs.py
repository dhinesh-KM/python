import database as db
class Student:

    def add_student(self, student_data):
        cursor = db.mycol.find().sort( {'_id': -1 } ).limit(1)
        last_id = cursor[0]['_id'] if db.mycol.count_documents({}) > 0 else 0
        _id = last_id + 1
        student_data["_id"]=_id
        x = db.mycol.insert_one(student_data)
        print(f"Student {student_data["name"]} added with ID: {x.inserted_id}")
        
    def add_mark(self,name):
        if db.mycol.count_documents({"name":name}) > 0:
            mark=[]
            avg = b = 0
            n = int(input("enter the no of subjects"))
        
            for i in range(1,n+1):
                a=float(input(f"enter mark{i}:"))  
                b += a
                mark.append(a)
            
            try:
                avg = b/n
                db.mycol.update_one({"name":name},{"$set" : {"mark":mark, "total": b, "average":avg}})
            
            except ZeroDivisionError as e:
                print("An error occured:",e)
        else:
            print(f"Student {name} doesn't not found")
        
    def display_average(self,name):
        cursor = db.mycol.find({"name":name},{"_id":0})
        
        for document in cursor:
            average = document.get("average")
            
            if average is not None:
                print(f"The average mark of {name} is {average}")
            else:
                print(f"{name} doesn't have mark to display average.")
                
    def display_total_average(self):
        total = count = avg = 0
        cursor = db.mycol.find({},{"_id":0})
        
        for document in cursor:
            tot = document.get("total")
            if tot is not None:
                count += 1
                total += tot
        avg = total/count
        
        if avg != 0:
            print(f"The average of whole students mark is {avg}")
        else:
            print(f"students doesn't have mark to display average.")
        
    def display_student(self,name):
        print("NAME\t\tAVERAGE\t\tMARK\t\t\t\tTOTAL")   
        print("------------------------------------------------------------------------------------------")
        if db.mycol.count_documents({"name":name}) > 0:
            cursor = db.mycol.find({"name":name},{"_id":0})
            for document in cursor:
                for value in document.values():
                    print(value,end="\t\t")
                print()
                
        else:
            print(f"Student {name} doesn't not found")
            
    def display_all(self):
        print("NAME\t\tAVERAGE\t\tMARK\t\t\t\t\tTOTAL")   
        print("------------------------------------------------------------------------------------------")
        cursor = db.mycol.find({},{"_id":0})
        for document in cursor:
            for value in document.values():
                print(value,end="\t\t")
            print()
        
    def delete_student(self,name):
        if db.mycol.count_documents({"name": name}) > 0:
            db.mycol.delete_one({"name":name})
            print(f"The document with the field name {name} has been deleted.")
            
        else:
            print(f"The document doesn't found.")
            
   
       
      
            
        
            
             
        
        