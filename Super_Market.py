class Market:
    __product_no = []
    __product_name = []
    __product_code = []
    __product_price = []
    __product_quantity = []

    def update(self):
        self.p = int(input("Enter Number of Products: ")) #3 products
    
        for i in range(self.p):
            pno = input("Enter Product name: ")
            pco = input("Enter product code: ") 
            ppo = input("Enter product price: ")
            pqo = input("Enter quantity of product: ")
            self.__product_no.append(i)
            self.__product_name.append(pno)
            self.__product_code.append(pco)
            self.__product_price.append(ppo)
            self.__product_quantity.append(pqo)
    
    def display(self):
        print('-----------------------------------------------------------------')
        print(' \nproduct_count \t product_name \t product_code \t product_price \t product_quantity')        
        for i in range(self.p):
            print("\t{count} \t\t {name} \t\t {code} \t\t {price} \t\t {quantity}".format(count=self.__product_no[i]+1,name=self.__product_name[i],code=self.__product_code[i],price=self.__product_price[i],quantity=self.__product_quantity[i]))
        print('-----------------------------------------------------------------')

    def print_bill(self):
        total = 0
        amount = 0
        print('------------------------------------------Invoice Bill----------------------------------------')
        print('\nproduct_count\tproduct_name\tproduct_code\tproduct_price\tproduct_quantity\tTotal')        
        for i in range(self.p):
            total = int(self.__product_quantity[i]) * int(self.__product_price[i]) 
            print("\t{count}\t\t{name}\t\t{code}\t\t{price}\t\t{quantity}\t\t{total}".format(count=self.__product_no[i]+1,name=self.__product_name[i],code=self.__product_code[i],price=self.__product_price[i],quantity=self.__product_quantity[i],total=total))
            amount = amount +  total
        print('-------------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------Total Amount = {}'.format(amount))    

ShopKeeper = Market()
ShopKeeper.update()
ShopKeeper.display()
ShopKeeper.print_bill()