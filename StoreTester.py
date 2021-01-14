# Dan Wu
# 1/13/2021
# contains unit tests for Store.py file which has at least five unit tests and use at least three different assert functions.

import unittest
import Store


class TestStore(unittest.TestCase):
    """Defines unit tests for the store"""

    def test_product(self):
        """ Test creating a product. """
        item = Store.Product(100,"Mango","Fruit",5,100 )
        self.assertAlmostEqual(item.get_title(),"Mango")
        self.assertAlmostEqual(item.get_description() , "Fruit" )
        self.assertAlmostEqual(item.get_price(),5)
        self.assertNotEqual(item.get_quantity_available(),99)
        self.assertIsNotNone(item)



unittest.main()
