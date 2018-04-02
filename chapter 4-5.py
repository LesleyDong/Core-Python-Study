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

#4.8.2-----------------------------------------------------------------------------------
>>> a = 3
>>> id(a)
1579861744
>>> a = 4
>>> id(a)
1579861776
>>> list = [1,2]
>>> id(list)
2289569091208
>>> list = [4,5]
>>> id(list)
2289569091080
>>> list = [1,4]
>>> id(list)
2289569091208
>>>
>>> id(list[1])
1579861776
>>> list[1] = list[1] + 1
>>> id(list[1])
1579861808
>>> id(list)
2289569091208
>>> list[1] = list[1] + 1
>>> id(list)
2289569091208
>>> list[0] = list[0] + 1
>>> id(list)
2289569091208
>>> a = 1
>>> id(a)
1579861680
>>> a = a + 1
>>> id(a)
1579861712

#5.4.1-----------------------------------------------------------------------------------
>>> a = 1 + 3j
>>> a.real
1.0
>>> a.imag
3.0
>>> a.conjugate
<built-in method conjugate of complex object at 0x0000021514F12C90>
>>> a.conjugate()
(1-3j)
>>>

#5.4.1-----------------------------------------------------------------------------------
>>> #cmp() in python2 but operator in python3
...
>>> import operator
>>> operator.gt(1,2)
False
>>> operator.gt(4,2)
True
>>> # greater than
...
>>> operator.ge(1,2)
False
>>> operator.ge(1,1)
True
>>> operator.gt(1,1)
False
>>> # greater than or equal
...
>>> operator.eq(1,1)
True
>>> operator.eq(5,8)
False
>>> #equal
...
>>> operator.lt(1,2)
True
>>> operator.le(1,2)
True
>>>#gt,ge,eq,lt,le


#5.6.2-----------------------------------------------------------------------------------
>>> int(4.55)
4
>>> complex(4)
(4+0j)
>>> int(4+1j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert complex to int
>>> float(5.33)
5.33
>>> float(int(5.33))
5.0
>>> long(3.52)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'long' is not defined
>>> long(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'long' is not defined
>>> complex(4,7)
(4+7j)
>>> bool(3)
True
>>> bool(0)
False
>>> bool(1+3j)
True
>>>
>>> abs(-1)
1
>>> abs(3+4j)
5.0
>>> coerce(3,3+j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'coerce' is not defined
>>> coerce(2,4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'coerce' is not defined
>>> divmod(1,6)
(0, 1)
>>> divmod(7,2)
(3, 1)
>>> pow(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pow expected at least 2 arguments, got 1
>>> pow(3,2)
9
>>> round(3)
3
>>> round(4.66442)
5
>>> round(3.42199)
3
>>>


#5.6.3-----------------------------------------------------------------------------------
>>> hex(45)
'0x2d'
>>> oct(45)
'0o55'
>>> hex(2+3j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'complex' object cannot be interpreted as an integer
>>>
>>> ord(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected string of length 1, but complex found
>>> ord(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected string of length 1, but int found
>>> ord('3')
51
>>> ord('a')
97
>>> chr(73)
'I'
>>>


# 5.7.2 Important!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
