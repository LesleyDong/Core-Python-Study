
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
