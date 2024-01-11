class RangeChecker:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def check_range(self, value):
        assert self.min_value <= value <= self.max_value, f"Value must be between {self.min_value} and {self.max_value}"

# Example usage:
range_checker = RangeChecker(10, 20)

try:
    range_checker.check_range(15)
except AssertionError as e:
    print(f"AssertionError: {e}")
