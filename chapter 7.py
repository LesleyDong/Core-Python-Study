
# 6.1.2 -----------------------------------------------------------------------------------------
>>> dicta = {}
>>> dictb = {1,"sxd",[11,22],(33,44)}
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dictb = {1,"sxd",[11,22],(33,44)}
TypeError: unhashable type: 'list'
>>> dictc = {1,"sxd",(11,22),(33,44)}
>>> 
