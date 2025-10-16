import sys
from pkg.calculator import Calculator
from pkg.renderer import render

def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print("Usage: python calculator.py '<expression>'")
        print("Example: python calculator.py '3+5*2'")
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()