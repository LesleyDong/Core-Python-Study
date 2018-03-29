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
