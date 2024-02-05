# 20-Inheritance
## Inherit
- 两个类相似的情况，可以使用继承
```
class <name> (<base class>):
	<suite>
```
- Dont repeat your self !

   ## Multiple Inheritance
   - 可以一次继承多个类
```
class <name> (<baseclass1>, <baseclass2>):
	<suite>
```

---
# 21-Representation

## Represatation
- 'str'：人类解释语言
- 'repr'：python解释语言
- 'eval'：返回传入字符串表达式的结果
```
half = Fraction(1, 2)
repr(half) # Fraction(1, 2)
str(half) # 1/2

repr(half) => half.__repr__()
str(half) => half.__str__()
```

## F-String 

```
from math import pi
print(f 'pi starts with {pi}' )

print('Ratio({0},{1})'.format(self.number,self.index))
```

- type(x)：实例repr可能会被修改，type保证取的是x所属类的repr
- __ repr __ (x)：x是self
- 若没有str属性，则用repr属性代替
```
def repr(x):
	return type(x).__repr__(x)
```

---
# 22-Composition

## Link List
```
s = Link(1, Link(2, Link(3)))
s.first = 5
t = s.rest
t.rest = s  #(5,2)循环
s.rest.rest.rest.rest.rest.first == 2
```
![image.png](https://cdn.jsdelivr.net/gh/LittleFish0403/Image@main/202402041709282.png)

```
def add(s, v)
	if s.first>v:
		s.first, s.rest = v, Link(s.first, s.rest)
	elif s.first<v and empty(s.rest):
		s.rest = Link(v)
	elif s.first<v:
		add(s.rest, v)
	return s
```

## Tree
- 数据抽象/面向对象都强调封装，将数据和方法组合在一起，以便于管理和隐藏实现细节。
- 而面向对象中抽象类是一种特殊的类，不能被实例化
---

