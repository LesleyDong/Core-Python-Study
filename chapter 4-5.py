#4.3.1-----------------------------------------------------------------------------------
>>> type(10)
<class 'int'>
>>> type(type)
<class 'type'>
>>>


#4.3.4-----------------------------------------------------------------------------------
>>> list = range(1:80)
  File "<stdin>", line 1
    list = range(1:80)
                  ^
SyntaxError: invalid syntax
>>> list = range(1,80)
>>> list[1:40:3]
range(2, 41, 3)
>>> for i in list[1:40:3]:
...     print(i)
...
2
5
8
11
14
17
20
23
26
29
32
35
38
>>> # Squence[start: end : step]    range(start, end, step)



#4.4.5-----------------------------------------------------------------------------------
>>> Ellipsis
Ellipsis
>>> None
>>>
>>> list[1:Ellipsis:30]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: slice indices must be integers or None or have an __index__ method
>>> list[1:None:30]
range(2, 80, 30)
>>>
>>> ...
Ellipsis


#4.5.2-----------------------------------------------------------------------------------
>>> a = 1
>>> b = a
>>> a is b
True
>>>
>>> c = 1
>>> a is c
True
>>> d = 0.5 + 0.5
>>> a is d
False
>>>


#4.6.4-----------------------------------------------------------------------------------
>>> def func(a):
...     if isinstance(a, (int)):
...             print("TURE")
...
>>> a = 3
>>> func(a)
TURE
>>> a=[1,2,3]
>>> func(a)
>>>
