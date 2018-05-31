
# 7.1 -----------------------------------------------------------------------------------------
>>> dicta = {}
>>> dictb = {1,"sxd",[11,22],(33,44)}
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dictb = {1,"sxd",[11,22],(33,44)}
TypeError: unhashable type: 'list'
>>> dictc = {1,"sxd",(11,22),(33,44)}
>>> dictd = {123,"sxd",(11,22),{1,2,3}}
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dictd = {123,"sxd",(11,22),{1,2,3}}
TypeError: unhashable type: 'set'
>>> 
>>> 
>>> 
>>> dicte = dict((1,2))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dicte = dict((1,2))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dictf = dict((["a":1],[34:11],[3:"b"]))
SyntaxError: invalid syntax
>>> dictf = dict((["a",1],[34,11],[3,"b"]))
>>> 
>>> dictf
{'a': 1, 34: 11, 3: 'b'}
>>> dictg = dict(([1,2,3],[4,5]))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dictg = dict(([1,2,3],[4,5]))
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> 

>>> dictf('a')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dictf('a')
TypeError: 'dict' object is not callable
>>> dictf['a']
1
>>> dictf['b']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    dictf['b']
KeyError: 'b'
>>> # 'a' is the key in dictf
>>> # use [] to get the key and refered value
>>> # if no key in this dict, return error

>>> 'a' in dictf
True
>>> 1 in dictf
False
>>> dictf.has_key('a')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dictf.has_key('a')
AttributeError: 'dict' object has no attribute 'has_key'
>>> dictc = {1,"sxd",(11,22),(33,44)}
>>> 1 in dictc
True
>>> 2 in dictc
False
>>> dictc[2]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dictc[2]
TypeError: 'set' object does not support indexing

>>> type(dictc)
<class 'set'>
>>> type(dictf)
<class 'dict'>
>>> type(dicta)
<class 'dict'>
＃The empty is dcit, like {xx,xx,xx,xx} is set, like{xx:xx, xx:xx, xx:xx} is dict

>>> dictf
{'a': 1, 34: 11, 3: 'b'}
>>> dictf[a]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dictf[a]
NameError: name 'a' is not defined
>>> dictf['a']
1
>>> 'a' in dictf
True
>>> 1 in dictf
False
>>> dictf.keys()
dict_keys(['a', 34, 3])
>>> dictf.values()
dict_values([1, 11, 'b'])
>>> dictf.items()
dict_items([('a', 1), (34, 11), (3, 'b')])
>>> for key in dictf:
	print(key)
	print(':')
	print(dictf[key])

	
a
:
1
34
:
11
3
:
b
>>> 


>>> dictf
{'a': 1, 34: 11, 3: 'b'}
>>> dicth = dict((["a",1],["a",2],["b",3]))
>>> dicth
{'a': 2, 'b': 3}
>>> dicth['a']
2
>>> dictj = {1:2,3:4,5:6,1:7}
>>> dictj
{1: 7, 3: 4, 5: 6}
>>> dictj[10] = 11
>>> dictj
{1: 7, 3: 4, 5: 6, 10: 11}
>>> 




# 7.2 -----------------------------------------------------------------------------------------
>>> dict1= {1:2}
>>> dict2= {1:3}
>>> dict3= {1:2,-1:-2}
>>> dict4= {2:2}
>>> dict1 < dict2
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    dict1 < dict2
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> import operator
>>> operator.gt(dict2,dict1)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    operator.gt(dict2,dict1)
TypeError: '>' not supported between instances of 'dict' and 'dict'
>>> dict5 = {"a":1}
>>> dict6 = {"b":2}
>>> dict5 < dict6
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    dict5 < dict6
TypeError: '<' not supported between instances of 'dict' and 'dict'
# Can Not be compared in python3


# 7.3 -----------------------------------------------------------------------------------------
>>> dict7 = dict((['x',i] for i in range (1,4)))
>>> dict7
{'x': 3}
>>> dict8 = dict(([i+1,i*i] for i in range (1,4)))
>>> dict8
{2: 1, 3: 4, 4: 9}
>>> len(dict7)
1
>>> len(dict8)
3
>>> 

>>> dict9 = {[2]:1}
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    dict9 = {[2]:1}
TypeError: unhashable type: 'list'
>>> dict9 = {(2):1}
>>> dict9 = {{2}:1}
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    dict9 = {{2}:1}
TypeError: unhashable type: 'set'
>>> dcit9 = { {2:3}:3}
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    dcit9 = { {2:3}:3}
TypeError: unhashable type: 'dict'
>>> hash([])
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    hash([])
TypeError: unhashable type: 'list'
>>> hash(())
3527539
>>> hash({})
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    hash({})
TypeError: unhashable type: 'dict'
>>> hash({1})
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    hash({1})
TypeError: unhashable type: 'set'
>>>

>>> dictff = dictf.copy()
>>> dictff
{'a': 1, 34: 11, 3: 'b'}
>>> id(dictf)
4317617248
>>> id(dictff)
4317615736
>>> dict10 = dictf.fromkeys()
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    dict10 = dictf.fromkeys()
TypeError: fromkeys expected at least 1 arguments, got 0
>>> dict10 = dictf.fromkeys(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    dict10 = dictf.fromkeys(1,2,3,4)
TypeError: fromkeys expected at most 2 arguments, got 4
>>> dict10 = dictf.fromkeys([1,2,3])
>>> dict10
{1: None, 2: None, 3: None}
>>> dictf
{'a': 1, 34: 11, 3: 'b'}
>>> dict10 = dictf.fromkeys([1,2],['a'])
>>> dict10
{1: ['a'], 2: ['a']}
>>> 

>>> dict11 = dictf.update(dict10)
>>> dict11
>>> dict11
>>> type(dict11)
<class 'NoneType'>
>>> dict11 = dictf.update(dict1)
>>> dict11
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None}
＃update will not return any value "NoneType"


>>> dict12 = dictf.setdefault('a',2)
>>> dict12
1
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None}
>>> dictf.setdefault(34)
11
>>> dictf.setdefault(1)
2
>>> dictf.setdefault("ff")
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None, 'ff': None}
>>> dictf.setdefault(3,"N")
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None, 'ff': None}
>>> dictf.setdefault('2018','0531')
'0531'
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None, 'ff': None, '2018': '0531'}
>>> dictf.get(34)
11
>>> dictf.get(54)
>>> dictf.get(54, "Not find")
'Not find'
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None, 'ff': None, '2018': '0531'}
>>> 
>>> dictf.popitem()
('2018', '0531')
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None, 'ff': None}
>>> 

>>> dictf.__sizeof__()
344
>>> dictf.popitem()
('ff', None)
>>> dictf
{'a': 1, 34: 11, 3: None, 1: 2, 2: None}
>>> dictf.__sizeof__()
344
>>> 
