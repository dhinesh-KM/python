from entity.product import Product,Discountedproduct

def add_product(inventory,product):
        
        inventory[product.get("ID")]=product
        
def remove_product(inventory,productid):
    if productid in inventory:
        inventory.pop(productid)
        print(f"product with the product_id={productid} has removed")
        
    else:
        print("The product_id you entered is not found")
        
def search_product(inventory,productname):   
    print("ID\t\tNAME\t\tPRICE\t\tQUANTITY\tDISCOUNT")   
    print("----------------------------------------------------------------------------------------")
    for x,y in inventory.items():
            for j in y:
                if inventory[x][j] == productname:
                    for i in inventory[x].values():
                        print(i, end="\t\t")
                    print()
                   


def display_inventory(inventory):   
    print("ID\t\tNAME\t\tPRICE\t\tQUANTITY\tDISCOUNT")   
    print("------------------------------------------------------------------------------------------")
    for x in inventory:
        for j in inventory[x]:
            print(inventory[x][j], end="\t\t")
    print(inventory)
        #print()
    print()
                
            
def update_product(inventory,product,productid):
        for x,y in inventory.items():
            for j in y:
                if inventory[x][j] == productid:
                    inventory[productid]=product
        print(f"product with the product_id = {productid} has updated \n")