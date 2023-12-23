LAB_SOURCE_FILE = __file__


def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    >>> my_map(lambda x: abs(x), [1, -1, 5, 3, 0])
    [1, 1, 5, 3, 0]
    >>> my_map(lambda x: print(x), ['cs61a', 'summer', '2023'])
    cs61a
    summer
    2023
    [None, None, None]
    """
    return [fn(x) for x in seq]

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    >>> my_filter(lambda x: (x + 5) % 3 == 0, [1, 2, 3, 4, 5])
    [1, 4]
    >>> my_filter(lambda x: print(x), [1, 2, 3, 4, 5])
    1
    2
    3
    4
    5
    []
    >>> my_filter(lambda x: max(5, x) == 5, [1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5]
    """
    return [x for x in seq if pred(x)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    result=seq[0]
    for x in seq[1:]:
        result = combiner(result,x)
    return result
    

def my_map_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(my_map)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.

    
    
def my_filter_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(my_filter)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    return  (lambda f: f(f)) (lambda f: lambda x: True if x%100 == 88 else (False if  x <=100 else f(f)(x//10)))(n)

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> s1 = [1, 3, 5]
    >>> s2 = [2, 4, 6]
    >>> merge(s1, s2)
    [1, 2, 3, 4, 5, 6]
    >>> s1
    [1, 3, 5]
    >>> s2
    [2, 4, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    >>> merge([2, 3, 4], [2, 4, 6])
    [2, 2, 3, 4, 4, 6]
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'merge', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    lst3 = lst1 + lst2
    def sort_times(lst,x):
        def sort_person(lst,m):
            if m == x-1:
                return lst
            if lst[m]>lst[m+1]:
                lst[m],lst[m+1] = lst[m+1],lst[m]
                return sort_person(lst,m+1)
            else:
                return sort_person(lst,m+1)
        lst = sort_person(lst,0)
        if x==1:
            return lst
        else:
            return sort_times(lst,x-1)
        
    return sort_times(lst3,len(lst3))

def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    def sum(term,x):
        if x==0:
            return 0
        else:
            return term(x)+sum(term,x-1)
    return sum(term,n)


def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    return len(list(filter(lambda x:x==True,list(map(lambda x:True if (len(x)%2==0 and x.lower()[0:len(x)//2]==x.lower()[len(x)-1:len(x)//2-1:-1])or(len(x)%2==1 and x.lower()[0:len(x)//2]==x.lower()[len(x)-1:len(x)//2:-1]) else False,L)))))

