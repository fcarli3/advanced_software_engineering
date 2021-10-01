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


def subtract(m,n):
    #TODO
    if(n < 0):
        for i in range(abs(n)):
            m += 1;
    else:
        for i in range(n):
            m -= 1;

    return m;


def multiply(m,n):
    #TODO
    res = 0;
    negativeRes = m > 0 and n < 0 or m < 0 and n > 0;

    n = abs(n);
    m = abs(m);

    for i in range(n):
        res += m;

    res = -res if negativeRes else res;

    return res;


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


def gcd(m,n):
    #TODO
    while(n != 0):
        tmp = n;
        n = m % n;
        m = tmp;

    return m;

def main():
    print('\nCalculator\n');

    sum_ = sum(10, 3);
    print("Sum: " + str(sum_));

    sub = subtract(6,-5);
    print("Subtract: " + str(sub));

    mul = multiply(5,-4);
    print("Multiply: " + str(mul));

    d = divide(4,2);
    print("Divide: " + str(d));

    great_common_div = gcd(6,36);
    print("GCD: " + str(great_common_div) + "\n");
    

if __name__ == "_main_":
    main();

