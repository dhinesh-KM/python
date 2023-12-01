class Product:
    key=1
    #def inputs(self,id,name,price,quantity):
        
    def add_product(self,inventory,product):
        product["ID"]=self.key
        inventory[self.key]=product
        self.key+=1
        
    def remove_product(self,inventory,productid):
        if productid in inventory:
            inventory.pop(productid)
            print(f"product with the product_id={productid} has removed")
        
        else:
            print("The product_id you entered is not found")
        
    def search_product(self,inventory,productname):   
        for x,y in inventory.items():
            for j in y:
                if inventory[x][j] == productname:
                    print(x,y)  
    
    def display_inventory(self,inventory):
        for x,y in inventory.items():
            print("product:",x,y)
            
    def update_product(self,inventory,product,productid):
            for x,y in inventory.items():
                for j in y:
                    if inventory[x][j] == productid:
                        inventory[x]=product
            print(f"product with the product_id = {productid} has updated \n",inventory[productid])
                        
    def get_id(self):
        print("ID: ",)

        
            
                    
            
p=Product()
inventory={}

while True:
    print("INVENTORY MANAGEMENT SYSTEM")
    print("----------------------------------")
    print("1. Add Product")
    print("2. Display Product")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Update Product")
    #print()
    print("choice")
    c=int(input())
    if c==1:
        try:
            print("Enter the product name,price,quantity:\n")
            name=str(input("Enter the product name:\n"))
            price=float(input("Enter the product price:\n"))
            quantity=int(input("Enter the product quantity:\n"))
            product={"ID":None,"NAME":name,"PRICE":price,"QUANTITY":quantity}
        
        except ValueError as e:
            print("An error occured:",e)
        p.add_product(inventory,product)

    elif c==2:
        p.display_inventory(inventory)
        
    elif c==3:
        productid=int(input("enter the productid to delete:"))
        p.remove_product(inventory,productid)
        
    elif c==4:
        productname=str(input("enter the productname to search:"))
        p.search_product(inventory,productname)
        
    elif c==5:
        p_id=int(input("Enter the product id to update:\n"))
        print()
        if p_id in inventory:
            print("1.  Update price\n2.  Update quantity\n3. Update Both")
            c=int(input("Enter your choice:"))
            if c==1:
                price=float(input("Enter the product price:\n"))
            elif c==2:
                quantity=int(input("Enter the product quantity:\n"))
            else:
                price=float(input("Enter the product price:\n"))
                quantity=int(input("Enter the product quantity:\n"))
                
            product={"ID":p_id,"NAME":name,"PRICE":price,"QUANTITY":quantity}
            p.update_product(inventory, product,p_id)
            
        else:
            print("The product_id you entered is not found")
            
        
        
    
    elif c==6:
        break
    
    else:
        print("Incorrect choice")
    
    




