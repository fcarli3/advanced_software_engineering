# calculator.py

def sum(m,n):
    #TODO
    if(n < 0):
        for i in range(abs(n)):
            m -= 1;
    else:
        for i in range(n):
            m += 1;

    return m;

def divide(m,n):
    #TODO
    res = 0;
    negativeRes = m > 0 and n < 0 or m < 0 and n > 0;

    n = abs(n);
    m = abs(m);

    while (m - n >= 0):
        m -= n;
        res += 1;

    res = -res if negativeRes else res;

    return res;


def main():
    print('\nCalculator\n');

    s = sum(10.5, 3);
    print("Sum: " + str(s));

    d = divide(4,7);
    print("Divide: " + str(d) + "\n");

main();

