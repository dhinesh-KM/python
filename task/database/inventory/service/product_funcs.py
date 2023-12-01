from entity.product import Product,Discountedproduct 
import database as db


def add_product(product):
    x= db.mycol.insert_one(product)
   
        
def remove_product(productid):
    if db.mycol.count_documents({"ID": productid}) > 0:
        db.mycol.delete_one({"ID":productid})
        print(f"product with the product_id={productid} has been removed")
        
    else:
        print(f"The product_id {productid} not found")
        
def search_product(productname):   
    print("ID\t\tNAME\t\tPRICE\t\tQUANTITY\tDISCOUNT")   
    print("----------------------------------------------------------------------------------------")
    if db.mycol.count_documents({"NAME": productname}) > 0:
        cursor = db.mycol.find({"NAME": productname}, {"_id":0})
        for document in cursor:
            for value in document.values():
                print(value, end="\t\t")
            print()
    else:
        print(f"The product_name {productname}  is not found")
                   


def display_inventory():   
    print("ID\t\tNAME\t\tPRICE\t\tQUANTITY\tDISCOUNT")   
    print("------------------------------------------------------------------------------------------")
    if db.mycol.count_documents({}) > 0:
        cursor = db.mycol.find({},{"_id":0})
        for document in cursor:
            for value in document.values():
                print(value, end="\t\t")
            print()
    else:
        print(f"There is no document to display")
                
            
def update_product(productid):
    if db.mycol.count_documents({"ID": productid}) > 0:
        cursor = db.mycol.find({"ID":productid})
        for document in cursor:
            p_id = document.get("ID")
        
            print("1.  Update price\n2.  Update quantity\n3. Update discount\n4. Update all")
            update_choice = int(input("Enter your choice:"))
            
            if update_choice == 1:
                price = float(input("Enter the product price:\n"))
                quantity = document.get("QUANTITY")
                discount_percent = document.get("DISCOUNT")
                
                
            elif update_choice == 2:
                quantity = int(input("Enter the product quantity:\n"))
                price = document.get("PRICE")
                discount_percent = document.get("DISCOUNT")
                
            elif update_choice == 3:
                discount_percent=float(input("Enter the product discount percent:\n"))
                price = document.get("PRICE")
                quantity = document.get("QUANTITY")
                
            elif update_choice == 4:
                price = float(input("Enter the product price:\n"))
                quantity = int(input("Enter the product quantity:\n"))
                discount_percent=float(input("Enter the product discount percent:\n"))
                
            
            name = document.get("NAME")
            p=Discountedproduct(name,price,quantity,discount_percent)
            
            product={"ID": p_id, "NAME": name, "PRICE": p.get_price(),"QUANTITY": quantity, "DISCOUNT": discount_percent}
            db.mycol.update_one( {"ID": productid} , {"$set": product } )
            
            print(f"product with the product_id {productid} has been updated")
        
    else:
        print(f"The product_id {productid}  is not found")
    
    
    