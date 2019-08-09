import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being integer 10."""
        prod = Product('Test Product')
        self.assertIsInstance(prod.price, int)
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being integer 20."""
        prod = Product('Test Product')
        self.assertIsInstance(prod.weight, int)
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being float 0.5."""
        prod = Product('Test Product')
        self.assertIsInstance(prod.flammability, float)
        self.assertEqual(prod.flammability, 0.5)

    def test_default_product_identifier(self):
        """Test product identifier being integer between 1000000 and 9999999."""
        prod = Product('Test Product')
        self.assertIsInstance(prod.identifier, int)
        self.assertTrue(1000000 <=  prod.identifier <= 9999999)

    def test_generated_product_methods(self):
        """Tests stealability and explode methods for generated product"""
        prod = generate_products()[0]

        price_over_weight = prod.price / prod.weight
        if price_over_weight < 0.5:
            self.assertEqual(prod.stealability(), 'Not so stealable...')
        elif 0.5 <= price_over_weight < 1:
            self.assertEqual(prod.stealability(), 'Kinda stealable.')
        else:
            self.assertEqual(prod.stealability(), 'Very stealable!')

        flammability_times_weight = prod.flammability * prod.weight
        if flammability_times_weight < 10:
            self.assertEqual(prod.explode(), '...fizzle.')
        elif 10 <= flammability_times_weight < 50:
            self.assertEqual(prod.explode(), '...boom!')
        else:
            self.assertEqual(prod.explode(), '...BABOOM!!')

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme product generator and inventory reporter are the tops!"""
    def test_default_num_products(self):
        """Test default number of products in product generator being 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)
    def test_legal_names(self):
        """Tests validity of names for generated products"""
        products = generate_products()
        for i in range(len(products)):
            adjective_and_noun = products[i].name.split(' ')
            self.assertEqual(len(adjective_and_noun), 2)
            self.assertIn(adjective_and_noun[0], ADJECTIVES)
            self.assertIn(adjective_and_noun[1], NOUNS)

if __name__ == '__main__':
    unittest.main()