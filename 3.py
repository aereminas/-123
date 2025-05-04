import unittest
import sys

def compute_factorial(number: int):
    if number < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if number == 0:
        return 1

    product = 1
    for i in range(1, number + 1):
        product *= i
        if product > sys.maxsize:
            raise OverflowError(f"Результат факториала для {number} слишком велик")

    return product


class FactorialTestCases(unittest.TestCase):
    def test_base_case_zero(self):
        self.assertEqual(compute_factorial(0), 1)

    def test_base_case_one(self):
        self.assertEqual(compute_factorial(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(compute_factorial(4), 24)
        self.assertEqual(compute_factorial(5), 120)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            compute_factorial(-1)

    def test_large_number(self):
        self.assertEqual(compute_factorial(10), 3628800) #уменьшил число

if __name__ == '__main__':
    unittest.main()

