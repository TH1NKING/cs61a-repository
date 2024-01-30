# 17-Generator

## Yield
- 用yield代替return，可以返回多次
- 返回值是一个iterator

```
#yield from
for x in a:
	yield a

# 等价于
yield from a
```

- 获得一个单词中的所有字串
```
def prefixes(s):
	if s:
	yield from prefixer(s[:-1])
	yield s

def substrings(s):
	if s:
		yield from prefisxes(s)
		yield from substrings(s[1:])
```

## Example: partitions
```
def partitions(n, m):
	if n>0 and m>0:
		if n==m:
			yield str(m)
		for p in partiotions(n-m, m):
			yield p+'+'+str(m)
		yield from partitions(n, m-1)
```

---
# 18/19-Object/Attribute
## Class
```
calss <name>:
	name = XXX
	def dance():
		return XXX
	...
	<suite> #attributes
```

- 使用__init__初始化class
- self: A new instance of the class in create \#相当于一张等待书写的白纸
```
class Account:
	def __init__(self, account_holder): #Constructor
		self.balance = 0 
		self.holder = account_holder
```

## Attribute
- 类中的attribute值改变，所有实例的值跟着改变
- class中为function，instance中为method

---
# Ant

- 以类造类
- 将父类属性和函数传递给子类（用下面的函数继承）
```
class FireAnt(Ant):
or
class LongThrower(ThrowerAnt)
```

- 父类继承 (继承父类属性，或将变量传递给父类构造函数)
- super() 用于多重继承，当有多个继承出现时使用
```
class Chidren(Partents):
	def __init__ (self, value):
		super.__init__(value)
```


