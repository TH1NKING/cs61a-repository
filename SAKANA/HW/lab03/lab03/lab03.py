from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    last=x%10
    x=x//10
    while x!=0:
        if (last<x%10):
            return False
        last=x%10
        x=x//10
    return True
    


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i!=k+1:
        x=n%10
        n=n//10
        while x>n%10 and n!=0:
            x,n=n%10,n//10
        final = x
        i = i+1
    return final


def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"
    def compared(x,ax,bx,cx):
        a=abs(x-2**ax)
        b=abs(x-2**bx)
        c=abs(x-2**cx)
        min=a
        i = ax
        if b<=min:
            min=b
            i=bx
        if c<=min:
            min=c
            i=cx
        return i
            
    n=0
    if x-1>0:
        while x-2**n>0:
            n+=1.0
        power_of_two=2.0 ** compared(x,n-2,n-1,n)
    if x-1<0:
        while 2**n-x>0:
             n-=1.0
        power_of_two=2.0 ** compared(x,n,n+1,n+2)
    return power_of_two


def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    new_func = func
    if n==0:
        def f(x):
            return x
        return f
    while n!=1:
        new_func = composer(new_func,func)
        n-=1
    def f(x):
        return new_func(x)
    return f

def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    f = make_repeater(func,2)
    return f


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    """
    checker = lambda x: False
    i = 2
    while i<=n:
        if not checker(i):
            checker = (lambda f, i: lambda x: f(x) or x%i==0)(checker, i)
        i = i+1
    return checker
    
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker
    """
    def g(orignal_x):
        def f(x):
            if orignal_x % x ==0:
                return True
            else:
                return False
        flag=False
        i=2
        while i<=n and not flag:
            flag=f(i)
            i+=1
        return flag
    return g        
        
def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = 2
    while i<=n:
        if not checker(i):
            def outer(f,i):
                def inner(x):
                    return f(x) or x%i==0
                return inner
            checker = outer(checker,i)
        i = i+1
    return checker

