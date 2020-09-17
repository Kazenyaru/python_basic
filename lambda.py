def usingLambdaInFunc(lamb, arg):
    return lamb(arg)


print(usingLambdaInFunc(lambda x: 2*x, 5))


def double(x): return x*2


print(double(10))
