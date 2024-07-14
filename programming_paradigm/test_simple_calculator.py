from simple_calculator import SimpleCalculator 
import unittest

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition operation."""
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(-3, -4), -7)
        self.assertEqual(self.calc.add(-3, 4), 1)
        self.assertEqual(self.calc.add(3, -4), -1)

    def test_subtraction(self):
        """Test the subtraction operation."""
        self.assertEqual(self.calc.subtract(3, 4), -1)
        self.assertEqual(self.calc.subtract(-3, -4), 1)
        self.assertEqual(self.calc.subtract(-3, 4), -7)
        self.assertEqual(self.calc.subtract(3, -4), 7)


    def test_multiplication(self):
        """Test the multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(3, -4), -12)

    def test_division(self):
        """Test the division operation."""
        self.assertEqual(self.calc.divide(3, 4), 0.75)
        self.assertEqual(self.calc.divide(-3, -4), 0.75)
        self.assertEqual(self.calc.divide(-3, 4), -0.75)
        self.assertEqual(self.calc.divide(3, -4), -0.75)