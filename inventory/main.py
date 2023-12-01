from entity.product import Product,Discountedproduct
from service.product_funcs import *
inventory={}

while True:
    print("--------------------------------------------")
    print("        INVENTORY MANAGEMENT SYSTEM         ")
    print("--------------------------------------------")
    print("1. Add Product")
    print("2. Display Product")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Update Product")
    print("6. Exit")
    print()
    
    print("Enter your choice")
    c=int(input())
    if c==1:
        #print("Enter the product name,price,quantity:\n")
        name=str(input("Enter the product name:\n"))
        price=float(input("Enter the product price:\n"))
        quantity=int(input("Enter the product quantity:\n"))
        print("If this product has a discount percent then enter 'a' & the discount percent else enter 'q'")
        s=input()
            
        if s == 'q':
            print("User skipped the discount percent")
            discount_percent=0
               
        elif s == 'a':
            discount_percent=float(input("Enter the product discount percent:\n"))
                
        p=Discountedproduct(name,price,quantity,discount_percent)
        add_product(inventory,p.product)

    elif c==2:
        display_inventory(inventory)
        
    elif c==3:
        productid=int(input("enter the productid to delete:"))
        remove_product(inventory,productid)
        
    elif c==4:
        productname=str(input("enter the productname to search:"))
        for x in inventory.values():
            if x["NAME"] == productname:
                search_product(inventory,productname)
                break
        else:
            print("The product_name you entered is not found")
       
        
    elif c==5:
        product_id=int(input("Enter the product id to update:\n"))
        print()
        if product_id in inventory:
            print("1.  Update price\n2.  Update quantity\n3. Update Both")
            update_choice=int(input("Enter your choice:"))
            
            if update_choice == 1:
                price = float(input("Enter the product price:\n"))
                quantity = inventory[product_id]["QUANTITY"]
            elif update_choice == 2:
                price = inventory[product_id]["PRICE"]
                quantity = int(input("Enter the product quantity:\n"))
            elif update_choice == 3:
                price = float(input("Enter the product price:\n"))
                quantity = int(input("Enter the product quantity:\n"))
            
            discount_percent= inventory[product_id]["DISCOUNT"]
            p=Discountedproduct(name,price,quantity,discount_percent)
            p.product["ID"]=product_id;   p.product["NAME"]= inventory[product_id]["NAME"]
            update_product(inventory, p.product,product_id)
         
            
        else:
            print("The product_id you entered is not found")
    
    elif c==6:
        break
    
    else:
        print("Incorrect choice")