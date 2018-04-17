
# 6.1.2 -----------------------------------------------------------------------------------------
>>> seq = [ 34, "adc", [1.5], ("ad",3), {44}]
>>> seq[3]
('ad', 3)
>>> seq[0]
34
>>> seq[0:3]
[34, 'adc', [1.5]]
>>> seq * 2
[34, 'adc', [1.5], ('ad', 3), {44}, 34, 'adc', [1.5], ('ad', 3), {44}]
>>> [1,5] in seq
False
>>> {44} in seq
True
>>> seq[::-1]
[{44}, ('ad', 3), [1.5], 'adc', 34]
>>> seq[::2]
[34, [1.5], {44}]
>>> seq[0:4:2]
[34, [1.5]]
>>> seq[1:100]
['adc', [1.5], ('ad', 3), {44}]
>>> seq[100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> seq[2:-2]
[[1.5]]
>>> seq[0:-2]
[34, 'adc', [1.5]]
>>> seq[:None]
[34, 'adc', [1.5], ('ad', 3), {44}]
>>> [None]
[None]
>>> [None]+range(-1,-4,-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "range") to list
>>>


# 6.1.3 -----------------------------------------------------------------------------------------
>>> a = list(seq)
>>> a
[34, 'adc', [1.5], ('ad', 3), {44}]
>>> b = tuple(seq)
>>> b
(34, 'adc', [1.5], ('ad', 3), {44})
>>> seq
[34, 'adc', [1.5], ('ad', 3), {44}]
>>>
>>> str("3")
'3'
>>> str(12)
'12'
>>>


#6.1.3 -----------------------------------------------------------------------------------------
>>> a =[1,"aa",{342,55},[21,55],("aad",32)]
>>> len(a)
5
>>> max(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
  >>> b = [1,4,5,52]
>>> max(b)
52
>>> min(b)
1
>>> sum(b)
62
>>> reversed(a)
<list_reverseiterator object at 0x00000137ABC6BF60>
>>> reversed(b)
<list_reverseiterator object at 0x00000137ABC6BF98>
>>> zip(a)
<zip object at 0x00000137ABC78208>
>>> a.reverse()
>>> a
[('aad', 32), [21, 55], {342, 55}, 'aa', 1]
>>> a.reversed()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'reversed'
  >>> for i in reversed(a):
...     print(i)
...
1
aa
{342, 55}
[21, 55]
('aad', 32)
>>> a.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'list' and 'tuple'
>>> b.sort()
>>> b
[1, 4, 5, 52]
>>> sort(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sort' is not defined
>>>


#6.3.2 -----------------------------------------------------------------------------------------
If the starting or ending index is not specified, the first and last index of the string are the default values, respectively.
>>> str = "abcd"
>>> str[0]
'a'
>>> # 0 is the first index
...
>>> str[3]
'd'
>>> len(str)-1
3
>>> # len(string)-1 is the last index
...


#6.3.2 -----------------------------------------------------------------------------------------
>>> import string
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'

#6.3.2 -----------------------------------------------------------------------------------------
# check if the title is valid
>>> def checkstr(str):
...     alphas = string.ascii_letters + "_"
...     num = string.digits
...     if str[0] not in alphas:
...             return 0
...     else:
...             for ch in str:
...                     if ch not in alphas + num:
...                             return 0
...             return 1
...
>>> checkstr("_sde")
1
>>> checkstr("12de")
0
>>> checkstr("sd--")
0
>>>
