"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""

# import pytest
# import sys
# from src.calculator import add, divide, subtract, multiply, power, square_root

import pytest
import subprocess
import sys
from src.calculator import add, divide, subtract, multiply, power, square_root


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2


class TestMultiplyDivide:
    """Test multiplication and division operations"""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(3, 4) == 12
        assert multiply(7, 8) == 56

    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, 2) == -5
        assert divide(-12, -3) == 4


class TestAdvancedOperations:
    """Test power and square root operations"""

    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers"""
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4

    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises
        ValueError"""
        with pytest.raises(ValueError):
            square_root(-4)


class TestCLIIntegration:
    """CLI + Calculator integration tests"""

    def run_cli(self, *args):
        """Run CLI and capture output"""
        cmd = [sys.executable, "-m", "src.cli"] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=".", check=False  # nosec
        )
        return result

    def test_cli_add(self):
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract(self):
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_subtract_missing_operand(self):
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Unexpected error:")

    def test_cli_multiply(self):
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"

    def test_cli_divide(self):
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "1.67"


# TODO: Students will add TestMultiplyDivide class
