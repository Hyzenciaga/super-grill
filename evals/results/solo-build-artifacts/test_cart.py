import unittest
from cart import subtotal

class CartTests(unittest.TestCase):
    def test_three_items(self):
        self.assertEqual(subtotal(120, 3), 360)

    def test_zero_quantity(self):
        self.assertEqual(subtotal(120, 0), 0)

    def test_zero_price(self):
        self.assertEqual(subtotal(0, 3), 0)

if __name__ == "__main__":
    unittest.main()
