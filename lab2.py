import lab1 as c

class FooCalculator:

    # empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

if __name__ == "_main_":
    calculator = FooCalculator();
    print("\nSum: " + str(calculator.sum(10,5)));
    print("Divide: " + str(calculator.divide(10,5)));