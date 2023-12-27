# 11-Sequence

- for < suite > in < expression >
  (for x,y in sequence )
## List Comprehensions（迭代式）
- \[ x+1 for x in odds ]
- \[ x for x in odds if 25 % x == 0 ]
- \[ x for x in range(2, n) ]
- \[out_exp_res  for  out_exp  in  input_list  (if condition) ]
- \[ 表达式  for  变量  in  列表  (条件) ]

## \*Dict/ Set/Tuple
- { key_expr: value_expr for value in collection if condition }
- { expression for item in Sequence if conditional }
- (expression for item in Sequence if conditional )

---
# 12-Container
## Slicing
- sum ( iterable \[ ,start ] )
- max ( iterable \[ ,key=func ] )
- all ( iterable ) -> bool_

## Dictionaries
- 输出键 : list( numerals )
- 输出值 : numerals.values()

--- 
# 13-Abstraction

## Abstract data
Compound objects combine objects togrther（数据集合）
Isolate two parts of any program that uses data 
- how data are presented（表示方式）
- how data are manipulated（操作方式）
**A methodology by which functions enforce an abstraction barrier between representation and use**

## Pairs
获取unit元素的方法
- A List Literal: Comma-separated expressions in brackets
	- pairs = \[1, 2]
- Unpacking a List: 
	- x, y = pairs
- Element Selection Operator:
	- x = pairs\[0]
- Element Selection Function:
	- getitme( pair, 0 )
 
## Abstraction Barriers
- 不可以直接跨越抽象障碍进行操作  **这种思想似乎非常重要**
![image.png](https://cdn.jsdelivr.net/gh/LittleFish0403/Image@main/202312271514430.png)

- 我想抽象的意义应该在于可以单独修改函数的某一部分而不影响整体，并且提升了代码的可阅读性

---
# Lab04
### Count Palindromes (单行实现回文字检测)
The Python library defines `filter`, `map`, and `reduce`, which operate on Python sequences. Devise a function that counts the number of palindromic words (those that read the same backwards as forwards) in a tuple of words using only `lambda`, basic operations on strings, the tuple constructor, conditional expressions, and the functions `filter`, `map`, and `reduce`. 
- 只用一行 ( filter, map, reduce ) 实现回文字检测
```
def count_palindromes(L):
    return len(list(filter(lambda x:x==True,list(map(lambda x:True if (len(x)%2==0 and x.lower()[0:len(x)//2]==x.lower()[len(x)-1:len(x)//2-1:-1])or(len(x)%2==1 and x.lower()[0:len(x)//2]==x.lower()[len(x)-1:len(x)//2:-1]) else False,L)))))
```
