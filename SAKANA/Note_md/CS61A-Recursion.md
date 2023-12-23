# 9_Recursion
## Leap of Faith

1. Verify the base case (n=0)
2. Treat fact as a functional abstraction (功能抽象)
3. Assume fact(n-1) is correct ,verify that fact(n) is correct (*数学归纳法*)

- When approaching or debugging recursive functions, you should avoid visualizing them in this way for large or complicated inputs, since the large number of frames can be quite unwieldy and confusing.

# 10_Tree_Recuersion
## Count_Partitions
<!--more-->
```
def count_partiotion(n,m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = conut_partitions(n-m,m)
		without_m = count_partitions(n,m-1)
		return with_m + without_m
```

# HW03

### Count Coins(Abstract)
Given a positive integer `total`, a set of coins makes change for `total` if the sum of the values of the coins is `total`. Here we will use standard US Coin values: 1, 5, 10, 25. 
```
def next_smaller_coin(coin):
	if coin == 25: 
		return 10 
	elif coin == 10: 
		return 5 
	elif coin == 5: 
		return 1

def count_coins(total):
	def constrained_count_small(total, largest_coin): 
	if total == 0: 
		return 1 
	if total < 0: 
		return 0 
	if largest_coin == None: 
		return 0 
		without_coin=constrained_count_small(total,next_smaller_coin(largest_coin)) 
		with_coin = constrained_count_small(total - largest_coin, largest_coin) 
		return without_coin + with_coin 
	return constrained_count_small(total, 25)

```

- 抽象的作用
- 仅关心当前函数能实现什么，而不提前构思函数的具体情况
- count_coins用处就是计算金额的组成情况
- without_coin和with_coin分别代表前半部分的情况和后半部分情况
- 直到细分到最后再开始分类讨论

### Towers of Hanoi(汉诺塔)
```
def print_move(origin, destination):
	print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
	if n == 1: 
		print_move(start, end) 
	else: 
		other = 6 - start - end 
		move_stack(n-1, start, other) 
		print_move(start, end) 
		move_stack(n-1, other, end)
```

### Anonymous Factorial(匿名阶乘)
```
def make_anonymous_factorial():
	return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
```

