from entity.product import Product,Discountedproduct
from service.product_funcs import *
inventory=[]
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
    
    print("Enter your choice:\n ")
    try:
        c=int(input())
        if c==1:
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
            product={"ID": p.get_id(), "NAME": p.get_name(), "PRICE": p.get_price(),"QUANTITY": p.get_quantity(), "DISCOUNT": discount_percent}
            add_product(product)

        elif c==2:
            display_inventory()
        
        elif c==3:
            productid=int(input("enter the productid to delete:"))
            remove_product(productid)
        
        elif c==4:
            productname=str(input("enter the productname to search:"))
            search_product(productname)
            
        elif c==5:
            product_id=int(input("Enter the product id to update:\n"))
            update_product(product_id)
    
        elif c==6:
            break
    
        else:
            print("Incorrect choice")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")