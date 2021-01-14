# Dan Wu
# 1/13/2021
# To write an online store simulator. it will have the following classes: Product which has ID code, title, description, price and quantity available;
# Customer: which has customer name, account ID.  Store: which has some number of products in inventory and number of customers as member

class Product :

   """Product object represents a product with an ID code, title, description, price and quantity available"""

   def __init__(self,ID_code,title,description,price,quantity_available):
       """Takes as parameters five values with which to initialize the Product"""
       self._ID_code = ID_code
       self._title = title
       self._description = description
       self._price = price
       self._quantity_available = quantity_available

   def get_ID_code(self):
       """get the current product ID code"""
       return self._ID_code

   def get_title(self):
       """get the title of the product"""
       return self._title

   def get_description(self):
       """get the product description"""
       return self._description

   def get_price(self):
       """get the product price"""
       return self._price

   def get_quantity_available(self):
       """get the currently available quantity"""
       return self._quantity_available

   def decrease_quantity(self):
        """represents when a product was sold"""
        self._quantity_available-=1
        return self._quantity_available

class Customer:
    """Represents a customer object represents a customer with a name and account ID, also customer must be a store member to purchase.
    premium customer get free shipping"""
    def __init__(self,customer_name,account_ID,premium_status):
        """take parameters to initialize the customer"""
        self._customer_name = customer_name
        self._account_ID = account_ID
        self._premium_status = premium_status
        self._cart = []

    def get_customer_name(self) :
        """get the name of the customer"""
        return self._customer_name

    def get_account_ID(self) :
        """get the account ID of the customer"""
        return self._account_ID

    def get_cart(self) :
        """get the product price"""
        return self._cart

    def is_premium_member(self):
        """returns whether the customer is premium member """
        return self._premium_status

    def add_product_to_cart(self,ID_code):
        """add product item to shopping cart"""
        return self._cart.append(ID_code)

    def empty_cart(self):
        """represents the action of emptying the shopping cart"""
        self._cart=[]

class Store:
    """represents a store, which has some number of products in its inventory and some number of customers as members."""
    def __init__(self,inventory, members):
        """take parameters to initialize the store"""
        self.inventory = dict()
        self.members = dict()


    def add_product(self,prod):
        """represents the action of adding product to store invnetory"""
        return self.inventory[prod.get_ID_code()]

    def add_member(self,mem):
        """represents the action of adding customer to store member list"""
        return self.members[mem.get_account_ID()]

    def get_product_from_id(self,ID_code):
        """represents action that take a product ID and returns the product with the matching ID, returns None if no product is found"""
        for p in self.inventory:
            if ID_code == p.get_ID_code():
                return p
        return None

    def get_member_from_id(self , account_ID) :
         """represents action that take a customer ID and returns the customer with the matching ID, returns None if no customer is found"""
         for c in self.members :
             if account_ID == c.get_account_ID():
                return c
         return None

    def product_search(self,search_term):
       """search string and returns a sorted list of ID codes for every product in the inventory
        whose title or description contains the search string"""
       id_list = []
       for x in self.inventory:
        title = self.inventory[x].get_title()
        description = self.inventory[x].get_description()
        if search_term.lower() in title.lower() or search_term.lower() in description.lower():
            id_list.append(x)
       return sorted(id_list)

    def add_product_to_member_cart(self,ID_code,account_ID):
        """represents the action to check if there is product and if there is member and complete the adding to cart action"""
        if ID_code not in self.inventory:
            return "product ID not found"
        if account_ID not in self.members:
            return "member ID not found"
        if self.inventory[ID_code].get_quantity_available()>0:
            self.members[account_ID].add_product_to_cart(ID_code)
            return "product added to cart"



    def check_out_member(self,account_ID):
        """check the customer member status, if customer is not member raise error alert,
        if customer is premium member shipping cost is 0 dollar otherwise shipping cost is 7% of the total cost of the items;
        empty the shopping cart once customers are charged"""

        class InvalidCheckoutError ( Exception ) :
            """define invalidcheckouterror exception"""
            pass

        if account_ID not in self.members:
            raise(InvalidCheckoutError())
        charge = 0
        account_ID = self.members[account_ID]
        for account_ID in account_ID.get_cart():
            product = self.inventory[ID_code]
            if product.get_quantity_avialable()>0:
                charge+=product.get_price()
                product.decrease_quantity()
        if not account_ID.is_premium_member():
            charge +=0.07*charge
        account_ID.empty_cart()
        return charge

def main():
     try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Customer("Yinsheng", "QWF", False)
        print(c1.check_out_member())
     except InvalidCheckoutError :
         print ( "You are not a member of this store." )

if __name__ =="_main_":
            main()








