import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_bad_shares(self):
        s = stock.Stock("GOOG", "100", 490.1)
        with self.assertRaises(TypeError):
            s.shares = 1000
        self.assertEqual(s.shares, 1200)


if __name__ == "__main__":
    unittest.main()
