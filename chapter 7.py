
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
>>> dictc[1]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dictc[1]
TypeError: 'set' object does not support indexing
>>> 
