def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3

def cycle(f1, f2, f3):
    def f(n):
        if n==0:
            def g(x):
                return x
        elif n==1:
            def g(x):
                return f1(x)
        elif n==2:
            def g(x):
                return f2(f1(x))
        elif n==3:
            def g(x):
                return f3(f2(f1(x)))
        elif n==4:
            def g(x):
                return f1(f3(f2(f1(x))))
        else:
            def fn(n,x):
                while n!=0:
                    if n==0:
                        return f1
                    elif n%3==0:
                        return f3(fn(n-1))
                    elif n%3==1:
                        return f1(fn(n-1))
                    elif n%3==2:
                        return f2(fn(n-1))
            h = fn(n)
            def g(x):
                return h(x)   
        return g
    return f

my_cycle = cycle(add1, times2, add3)
do_two_cycles = my_cycle(6)
do_two_cycles(1)