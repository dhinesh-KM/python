class Product:
    key=0
    product={}
    def __init__(self,name,price,quantity):
        Product.key+=1
        self.__id=Product.key
        self.__name=name  
        self.__price=price  
        self.__quantity=quantity  
        
        self.product={"ID":self.__id,"NAME":self.__name,"PRICE":self.get_price(),"QUANTITY":self.__quantity}
        
    
                        
    def get_id(self):
        return self.__id 
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def set_id(self,new_value):
        self.__id = new_value
    
    def set_name(self,new_value):
        self.__name = new_value
    
    def set_price(self,new_value):
        self.__price = new_value
    
    def set_quantity(self,new_value):
        self.__quantity = new_value
        
class Discountedproduct(Product):
    def __init__(self,name,price,quantity,discountpercentage):
        self.discount_percentage=discountpercentage
        super().__init__(name,price,quantity)
        self.product["DISCOUNT"]=self.discount_percentage
            
        
    def get_price(self):
        discount=super().get_price()*(self.discount_percentage/100)
        discounted_price = super().get_price()-discount
        return discounted_price
    

        
            
                    
            

    
    




