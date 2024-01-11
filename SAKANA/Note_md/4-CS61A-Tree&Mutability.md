# 14-Tree
## Construction
![image.png](https://cdn.jsdelivr.net/gh/LittleFish0403/Image@main/202401031116553.png)

## Tree Abstraction
tree( 3, \[ tree( 1 ), tree ( 2, \[ tree( 1 ), tree( 1 ) ] ) ]

## Sum Path

- 将n作为计数器，用k叠加
```
def fact_times(n, k):
	if n==0:
		return k
	else:
		return fact_times(n-1, k*n)
```


---
# 15-Mutability
## Objects
- name . attribute

## Mutability List
- arrayx 与 array 始终相同 （同一对象）
```
array=[1,2,3,4,5]

arrayx = array

array.pop()

array.append(1)

array.extend([8,9])
...
print(arrayx)
```

- Mutation: 突变，指对象发生变化

## Tuples（不可变列表）

- 基础语法
```
(3, 4, 5, 6)
tuple([ 3, 4, 5 ])
(2, ) #单个元素元组
```

- 若元组中的元素可变（如列表），则可以修改

## Identity
- is : 对象相同
- == : 数值上相等

PS：默认参数值是同一个，反复调用同一函数导致默认参数值突变可能会出错



---
# 16-Iterators(迭代器)
## List Iterator
- 进入迭代：x = iter( \[list] ) 
- 下一个值：next ( t )
- 输出剩余值：list ( t )
```
s=[ 3, 4, 5 ]
t = iter(s) #t进入迭代,t=3
next(t) #t=4
next(t) #t=5

u = iter(s) #新的迭代,u=3
```

## Dic Iterator 
- 迭代键：k = iter( d.keys( ) )  # or iter( d )
- 迭代值：v = iter( d.values( ) )
- 迭代键值对：i = iter( d.items( ) )

PS：迭代期间字典大小不能发生变化（可以改变值）

## 'For' Statement
- for 语句同样推动迭代器迭代
- 被for/list 过的迭代器将失效
```
ri = iter( range(3,6) )
for r in ri:
	print(r) #ri 失效
```


