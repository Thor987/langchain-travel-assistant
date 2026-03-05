import unittest
from src.tools import calculate_budget, query_weather


class TestTools(unittest.TestCase):

    def test_budget_calculator_valid_input(self):
        result = calculate_budget("700,3")
        self.assertIn("2100", result)

    def test_budget_calculator_invalid_input(self):
        result = calculate_budget("invalid")
        self.assertIn("format error", result.lower())

    def test_weather_query(self):
        result = query_weather("Beijing")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
