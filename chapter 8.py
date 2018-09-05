>>> # if & else
>>> def fun1(i):
	if i > 3:
		print("a")
		if i > 5:
			print("b")
		else:
			print("c")

			
>>> def fun2(i):
	if i > 3:
		print("a")
		if i > 5:
			print("b")
	else:
		print("c")
    
>>> fun1(4)
a
c
>>> fun1(1) 
>>> fun2(4)
a
>>> fun2(1)
c

>>> # xrange() is better for larger range compared with range()


>>> # while for and else
>>> def fun3(i):
	while i > 1:
		if i > 3:
			print("a")
		else:
			print("b")
		i -= 1
	else:
		print("c")

		
>>>
>>> fun3(4)
a
b
b
c


>>> # next()
>>> l = [1,2,3]
>>> i = iter(l)
>>> i.next()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    i.next()
AttributeError: 'list_iterator' object has no attribute 'next'
>>> t = (1,2,3)
>>> i = iter(t)
>>> i.next()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    i.next()
AttributeError: 'tuple_iterator' object has no attribute 'next'
>>> i.__next__
<method-wrapper '__next__' of tuple_iterator object at 0x1057b1ef0>
>>> i.__next__()
1
>>> l = [1,2,3]
>>> ii = iter(l)
>>> ii.__next__()
1
>>> 
