# 8_Function Examples
# Implementing a Function
当你在面对template时可能出现的两种情况：
- 有用，在此基础上进行编写
- 无用，进行修改

在编写代码时明确productive strategy 以提高效率


# Decorator(HOF)
`trace`

```
//decration function

def trace1(fn):
	def traced(x):
	print("Calling",fn,"on agument",x)
	return fn(x)
return traced

@trace1
def triple(x):
	return 3*x
```

- 可以跟踪函数调用情况




# Lab03
##### Implement `div_by_primes_under`, which takes in an integer `n` and returns an n-divisibility checker. An _n-divisibility-checker_ is a function that takes in an integer k and returns whether `k` is divisible by any integers between 2 and `n`, inclusive. Equivalently, it returns whether `k` is divisible by any primes less than or equal to `n`.

```
#lamdda版本
def div_by_primes_under(n):
	checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker


#def版本
def div_by_primes_under_no_lambda(n):
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
```

- 回头再研究一下

