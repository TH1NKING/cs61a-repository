# 23-Efficiency
## Memoization
- 记住之前己算过的结果
```
def memo(f):
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized 
```

## Growth
- 使用不同的方法完成函数可以加快运行速率
- Exponential growth 指数增长
- Quadratic growth 二次增长
- Linear growth 线性增长
- Logarithmic growth 对数增长
- Constant growth 恒定增长

- 表示方法 $\theta$/O

# 24-Decomposition
- Module Design

# 25-Data Example
- append/extend: 突变，仅为copy
- addition/slicing: 非突变，t依旧是t
- pop(): 优先pop最后一个
- remove(): 优先remove第一个
- count(): 寻找num的个数

- map(func, list)
- filter(func, list)
- zip(list1, list2)

- any(list): 只要list中有一个为True，返回True
	- 元素除了是 0、空、False外都算True
- all(list): 要全部为True，返回True
```
#  获取列表相邻数字最大值
max( [s[i]+s[i+1] for i in range(len(s)-1) ] )
# 第二种
max( a+b for a,b in zip(s[:-1],s[1:]) )
```

```
# 将以数字d为结尾的s里的数字加入字典
{d:[x for x in s if x%10==d] for d in range(10) if any([x%10==d for x in s])}
```
---
