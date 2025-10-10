"""
Integration Tests - CLI + Calculator Working Together
"""

from click.testing import CliRunner
import pytest
from src.cli import calculate
from src.calculator import add, multiply, divide, power, square_root

class TestCLIIntegration:
    """Test CLI application integrating with calculator module."""

    def run_cli(self, *args):
        """Invoke Click CLI in-process so coverage is measured."""
        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    def test_cli_add_integration(self):
        """Test CLI add operation."""
        res = self.run_cli("add_cmd", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "8.0"

    def test_cli_multiply_integration(self):
        """Test CLI multiply operation."""
        res = self.run_cli("multiply_cmd", "4", "7")
        assert res.exit_code == 0
        assert res.output.strip() == "28.0"

    def test_cli_divide_integration(self):
        """Test CLI divide operation."""
        res = self.run_cli("divide_cmd", "15", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "5.0"

    def test_cli_sqrt_integration(self):
        """Test CLI sqrt operation."""
        res = self.run_cli("sqrt_cmd", "16")
        assert res.exit_code == 0
        assert res.output.strip() == "4.0"

    def test_cli_error_handling_integration(self):
        """Test CLI division by zero."""
        res = self.run_cli("divide_cmd", "10", "0")
        assert res.exit_code == 1
        assert "Cannot divide by zero" in res.output

    def test_cli_invalid_operation_integration(self):
        """Test CLI invalid command."""
        res = self.run_cli("invalid", "1", "2")
        assert res.exit_code != 0

class TestCalculatorModuleIntegration:
    """Test calculator module functions work together."""

    def test_chained_operations(self):
        """Test using results from one operation in another."""
        step1 = add(5, 3)  # 8
        step2 = multiply(step1, 2)  # 16
        step3 = divide(step2, 4)  # 4
        assert step3 == 4.0

    def test_complex_calculation_integration(self):
        """Test complex calculation using multiple functions."""
        a_squared = power(3, 2)  # 9
        b_squared = power(4, 2)  # 16
        sum_squares = add(a_squared, b_squared)  # 25
        hypotenuse = square_root(sum_squares)  # 5
        assert hypotenuse == 5.0
