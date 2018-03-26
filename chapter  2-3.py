#2.1.1 -------------------------------------------------------------------------------------------------
>>> sting = hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> sting = "hello"
>>> sting
'hello'
>>>
>>> print sting
  File "<stdin>", line 1
    print sting
              ^
SyntaxError: Missing parentheses in call to 'print'
>>> print(sting)
hello
>>> #python3 support print(xxx) instead of print xxx
>>>
>>>
>>> print("%s is % year old\n", "peter",18)
%s is % year old
 peter 18
>>> print("%s is %d" % ("petet",18))
petet is 18
>>> #"%d"  has the same usage of c/c++
>>>
>>>
>>> fp = open ("d:/python/abc.txt","a+")
>>> print("error",file=fp)
>>> fp.close()
>>>#The output is redirected to the log file “>>"


#2.2.1 -------------------------------------------------------------------------------------------------
>>> pin = input("pin:")
pin:123
>>> pin
'123'
>>> #"input" in python3 = "raw_input" in python2
>>>
>>>
>>> age = input("age :")
age :16
>>> print(age)
16
>>> print("%d" % age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %d format: a number is required, not str
>>> print("%d" % int(age))
16
>>> age = int (age)
>>> age
16
>>> print("%d" % age)
16
>>>#The default input type is string type, you have to trasfrom it to int type
>>>
>>>

#2.2.2 -------------------------------------------------------------------------------------------------
>>> _
'hello'
>>> a = 1
>>> b = 3
>>> c =a + b
>>> c
4
>>> _
4
>>> d = "aa"
>>> _
4
>>> d
'aa'
>>> _
'aa'
>>> #"_" show the value of the last function
...
>>> c= -c
>>> abs(c)
4
>>> c
-4
>>> _
-4
>>>


#2.4 -------------------------------------------------------------------------------------------------
>>> 1+2
3
>>> 1/6
0.16666666666666666
>>> 6/2
3.0
>>> 6//2
3
>>> 1//6
0
>>> 1-4
-3
>>> 3*5
15
>>> 2*4
8
>>> 2**4
16
>>> 2<5
True
>>> 2>6
False
>>> 1%4
1
>>> 8%3
2
>>> 2<4 and 2>3
False
>>> 2<4 and 2>1
True
>>> 2<4 or 2>1
True
>>> not 4>6
True
>>> 3 < 4 <5
True
>>> 3 < 4 < 3
False
>>>



#2.5 -------------------------------------------------------------------------------------------------
>>> name = "sheng"
>>> count = 0
>>> mile =6.54
>>> name = name +1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> count = count +2.3
>>> count
2.3
>>> count ++
  File "<stdin>", line 1
    count ++
           ^
SyntaxError: invalid syntax
>>> ++count
2.3
>>> --count
2.3
>>> #No support for a++ or a--
>>> Name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Name' is not defined
>>>#Sensitive to Uppercase and lowercase letters


#2.6-2.7 -----------------------------------------------------------------------------------------------
>>> # int/long/bool/float/complex
...
>>> str = "str"
>>> str[0]
's'
>>> str[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> str[2]
'r'
>>> str[1:2]
't'
>>> str= "abcdefg"
>>> str[3:6]
'def'
>>> str[-2]
'f'
>>> b = "hello"
>>> str + b
'abcdefghello'
>>> str[4:]
'efg'
>>> str *2
'abcdefgabcdefg'
>>>


#2.8-2.9 ------------------------------------------------------------------------------------------------
>>> #list
...
>>> aList = [1, "ad", 4.5, 3+1j]
>>> aList
[1, 'ad', 4.5, (3+1j)]
>>> aList[3]
(3+1j)
>>> # similar to the string
...
>>>
>>>
>>> #Tuple
...
>>> aTuple = (1, "ad",4.5, 2+4j)
>>> aTuple
(1, 'ad', 4.5, (2+4j))
>>> aTuple[2]
4.5
>>> aTuple[2:]
(4.5, (2+4j))
>>> aList[2:]
[4.5, (3+1j)]
>>> aTuple[1]
'ad'
>>> #dict
...
>>> aDict = { "aa" : 3}
>>> aDict[3] = "3a"
>>> aDict
{'aa': 3, 3: '3a'}
>>> aDict.keys
<built-in method keys of dict object at 0x000001ADC8321990>
>>> aDict.keys()
dict_keys(['aa', 3])
>>> aDict["aa"]
3
>>> a = "china"
>>> a[::-1]
'anihc'


#2.11-2.14 ------------------------------------------------------------------------------------------------
>>> #if
...
>>> a = 4
>>> if a > 3:
... a = a+1
  File "<stdin>", line 2
    a = a+1
    ^
IndentationError: expected an indented block
>>>#you have to print [tab] in front of the if-suite (like "a = a + 1")
>>> if a>3:
... a = a+2
  File "<stdin>", line 2
    a = a+2
    ^
IndentationError: expected an indented block
>>> if a>3:
...     a=a+2
... else:
...     a=8
...
>>> a
6
>>>#while
>>> while i <10:
...     print("i");
...     i=i+1
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined
>>> i = 0
>>> while i <10:
...     print("i");
... i = i+1
  File "<stdin>", line 3
    i = i+1
    ^
SyntaxError: invalid syntax
>>>
>>>
>>> while i <3:
...     print("i");
...     i = i+1
...
i
i
i
>>>#for
>>> for item in ["w","f","s"]:
...     print(item)
...
w
f
s
>>>>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> # range is a function to create a list
>>> for i in range(5,8):
...     print(i)
...
5
6
7
>>>
>>> for c in "abc":
...     print(c)
...
a
b
c
>>> for u ,c in enumerate("abc"):
...     print("%c %d" % (c,u))
...
a 0
b 1
c 2
>>>>>> seq = [ x**2 for x in range(8) if not x % 2]
>>> for i in seq:
...     print(i)
...
0
4
16
36
>>>




#2.15 ------------------------------------------------------------------------------------------------
>>> fp = open ("d:/python/abc.txt","r")
>>> for line in fp:
...     print(line)
...     fp.close()
...
error

(None,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> fp = open ("d:/python/abc.txt","r")
>>> for line in fp:
...     print(line)
...
error

acc

cde

>>> fp = open ("d:/python/abc.txt", "r")
>>> for line in fp:
...     print(line,end=" ")
...
error
 acc
 cde

 >>># use print(xxxx,end=" ") to Suppress line breaks
 
 
 #2.17 ------------------------------------------------------------------------------------------------
 >>> def double(x):
...     return x*2
...
>>>#def function_name([arguments]):
>>> double(4)
8
>>> def add(x = 1):
...     return x+1
...
>>> double("ad")
'adad'
>>># x=1 is the default value
>>> add()
2
>>> add(4)
5
>>>




 #2.18 ------------------------------------------------------------------------------------------------
>>> class CC(object):
...     ver=0.1
...     def _init_(self):
...             print(ver)
...     def add(x):
...             return x*2
...
>>> ccc = CC()
>>> ccc.add("11")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 1 positional argument but 2 were given
>>> ccc._init_()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in _init_
NameError: name 'ver' is not defined
>>>
>>>
>>> class CC(object):
...     ver = 0.1
...     def _init_(self):
...             print("init")
...             return
...     def add(self,x):
...             return x+1
...
>>> ccc=CC()
>>> ccc.ver
0.1
>>> ccc.add(3)
4
>>> ccc._init_()
init
>>>
>>>
>>>
>>>
>>> class A():
...     def __init__():
...             print("adc")
...
>>> a=A
>>> a=A()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes 0 positional arguments but 1 was given
>>> class A():
...     def __init__(self):
...             print("abc")
...
>>> a=A()
abc
>>> a.__class__.__name__
'A'
>>>
>>># the __init__ is like the constructor
>>># It must be remeber that there are two "_" instead of one in __init__
>>># It must be remeber that “self" is one of the arguments in the class function.
>>># the variable in the Class can't be used in the class function 




 #dir ------------------------------------------------------------------------------------------------
>>> type(dir)
<class 'builtin_function_or_method'>
>>> dir(sys)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sys' is not defined
>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_getframe', '_git', '_xoptions', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']
>>>

 #code style ------------------------------------------------------------------------------------------------
>>> a='''a
... b
... c
... '''
>>> a
'a\nb\nc\n'
>>> print(a)
a
b
c

>>>

>>> a = 1 + 1 \
... +2
>>> a
4
>>> x=4
>>> y=12
>>> x,y = y,x
>>>
>>> x
12
>>> y
4
>>>
>>> a,b,c = (1,c,"str")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> a,b,c = (1,'c',"str")
>>> a
1
>>> b
'c'
>>> c
'str'
>>> a,b,c
(1, 'c', 'str')
>>> a,b
(1, 'c')
>>>
>>> #del memory
...
>>> x = 1 #1
>>> z = y = x #3
>>> x=3;z=2 #1
>>>
>>> del y #0
>>> myList.remove(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myList' is not defined
>>> myList = [1,3,4]
>>> myList
[1, 3, 4]
>>> del myList
>>> myList
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myList' is not defined
>>> y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>>
