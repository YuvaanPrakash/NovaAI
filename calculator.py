"""
calculator.py
Offline Calculator Module for Nova AI
Supports:
- Basic arithmetic
- Scientific functions
- Algebra using SymPy
"""

import math
import sympy as sp


class Calculator:

    def calculate(self, expression: str):
        """
        Evaluate a mathematical expression.
        """

        expression = expression.lower().strip()

        # Replace common math symbols
        expression = expression.replace("^", "**")
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        try:
            # Square root
            if expression.startswith("sqrt"):
                number = float(expression.replace("sqrt", "").strip())
                return math.sqrt(number)

            # Factorial
            if expression.startswith("factorial"):
                number = int(expression.replace("factorial", "").strip())
                return math.factorial(number)

            # Trigonometry
            if expression.startswith("sin"):
                number = float(expression.replace("sin", "").strip())
                return math.sin(math.radians(number))

            if expression.startswith("cos"):
                number = float(expression.replace("cos", "").strip())
                return math.cos(math.radians(number))

            if expression.startswith("tan"):
                number = float(expression.replace("tan", "").strip())
                return math.tan(math.radians(number))

            # Logarithm
            if expression.startswith("log"):
                number = float(expression.replace("log", "").strip())
                return math.log10(number)

            # Algebra with SymPy
            if "=" in expression:
                left, right = expression.split("=")

                x = sp.Symbol("x")

                equation = sp.Eq(
                    sp.sympify(left),
                    sp.sympify(right)
                )

                solution = sp.solve(equation)

                return solution

            # Normal arithmetic
            return eval(expression)

        except Exception as e:
            return f"Calculation Error: {e}"


calculator = Calculator()


if __name__ == "__main__":

    while True:

        expr = input("Enter expression: ")

        if expr.lower() == "exit":
            break

        print("Answer:", calculator.calculate(expr))