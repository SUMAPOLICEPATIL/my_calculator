"""
Command-line interface for calculator module.
"""

import sys
import click
from src.calculator import add, multiply, divide, power, square_root

@click.group()
def calculate():
    """Calculator CLI."""
    pass

@calculate.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def add_cmd(x, y):
    """Add two numbers."""
    click.echo(add(x, y))

@calculate.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def multiply_cmd(x, y):
    """Multiply two numbers."""
    click.echo(multiply(x, y))

@calculate.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def divide_cmd(x, y):
    """Divide two numbers."""
    try:
        click.echo(divide(x, y))
    except ZeroDivisionError as e:
        click.echo(e, err=True)
        sys.exit(1)

@calculate.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def power_cmd(x, y):
    """Raise x to the power y."""
    click.echo(power(x, y))

@calculate.command()
@click.argument("x", type=float)
def sqrt_cmd(x):
    """Square root of a number."""
    try:
        click.echo(square_root(x))
    except ValueError as e:
        click.echo(e, err=True)
        sys.exit(1)

if __name__ == "__main__":
    calculate()
