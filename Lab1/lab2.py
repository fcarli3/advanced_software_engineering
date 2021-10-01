import lab1 as c

class FooCalculator:

    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def subtract(self, m, n):
        return c.subtract(m,n)

    def multiply(self, m, n):
        return c.multiply(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

    def gcd(self, m, n):
        return c.gcd(m,n)
        

calculator = FooCalculator();
print("\nSum: " + str(calculator.sum(10,5)));
print("Subtract: " + str(calculator.subtract(10,5)));
print("Multiply: " + str(calculator.multiply(10,5)));
print("Divide: " + str(calculator.divide(10,5)));
print("GCD: " + str(calculator.gcd(10,5)));