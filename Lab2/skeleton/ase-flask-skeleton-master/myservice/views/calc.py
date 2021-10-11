from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calc = JsonBlueprint('calc', __name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    #http://127.0.0.1:5000/calc/sum?m=4&n=3
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m

    if(n < 0):
        for i in range(abs(n)):
            result -= 1;
    else:
        for i in range(n):
            result += 1;

    return jsonify({'Result' : str(result)});


@calc.route('/calc/mul', methods=['GET'])
def multiply():
    
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    res = 0;
    negativeRes = m > 0 and n < 0 or m < 0 and n > 0;

    n = abs(n);
    m = abs(m);

    for i in range(n):
        res += m;

    res = -res if negativeRes else res;

    return jsonify({'Result' : str(res)});


@calc.route('/calc/div', methods=['GET'])
def divide():
    
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    res = 0;
    negativeRes = m > 0 and n < 0 or m < 0 and n > 0;

    n = abs(n);
    m = abs(m);

    while (m - n >= 0):
        m -= n;
        res += 1;

    res = -res if negativeRes else res;

    return jsonify({'Result' : str(res)});


@calc.route('/calc/concat', methods=['GET'])
def concat():
    p = str(request.args.get('p'))
    q = str(request.args.get('q'))

    result = str(p + q)

    return jsonify({'Result' : str(result)});
