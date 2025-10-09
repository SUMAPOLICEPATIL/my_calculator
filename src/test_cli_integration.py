# """
# Integration Tests - CLI + Calculator Working Together
# """

# import subprocess
# import sys
# import pytest

# class TestCLIIntegration:
#     """Test CLI application integrating with calculator module"""

#     def run_cli(self, *args):
#         """Helper method to run CLI and capture output"""
#         cmd = [sys.executable, "src/cli.py"] +list(args)
#         result = subprocess.run(
#             cmd,capture_output=True, text=True, cwd=".",check=False,shell=False
#         )
#         return result

#     def test_cli_add_integration(self):
#         """Test CLI can perform addition"""
#         result = self.run_cli("add", "5", "3")
#         assert result.returncode == 0
#         assert result.stdout.strip() == "8"

#     def test_cli_subtract_integration(self):
#         """Test CLI can perform subtraction"""
#         result = self.run_cli("subtract", "5", "3")
#         assert result.returncode == 0
#         assert result.stdout.strip() == "2"

#     def test_cli_subtract_missing_operand_error(self):
#         """Test CLI handles missing operand for subtraction gracefully"""
#         result = self.run_cli("subtract", "5")
#         assert result.returncode == 1
#         assert result.stdout.strip().startswith("Unexpected error:")

#     def test_cli_multiply_integration(self):
#         """Test CLI can perform multiplication"""
#         result = self.run_cli("multiply", "5", "3")
#         assert result.returncode == 0
#         assert result.stdout.strip() == "15"
#     def test_cli_divide_integration(self):
#         """Test CLI can perform division"""
#         result = self.run_cli("divide", "5", "3")
#         assert result.returncode == 0
#         assert result.stdout.strip() == "1.67"
# File: tests/integration/test_cli_integration.py

import pytest
import subprocess
import sys  # ✅ needed for run_cli
from src.calculator import add, subtract, multiply, divide, power, square_root
from src import cli


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output safely"""
        cmd = [sys.executable, "src/cli.py"] + list(args)
        # Bandit B603 warning safe here: we are passing only trusted args
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=".", check=False  # no shell=True
        )  # nosec: subprocess is used safely for testing
        return result

    def test_cli_add_integration(self):

        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):

        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_subtract_missing_operand_error(self):

        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Unexpected error:")

    def test_cli_multiply_integration(self):

        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"

    def test_cli_divide_integration(self):

        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "1.67"
