Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1= [1,2,3,4]
l2= [5,6,7,8]
l1.apprnd(l2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l1.apprnd(l2)
AttributeError: 'list' object has no attribute 'apprnd'. Did you mean: 'append'?
l1.append(l2)
l1
[1, 2, 3, 4, [5, 6, 7, 8]]
l1.append(7)
l1
[1, 2, 3, 4, [5, 6, 7, 8], 7]
l1.remove(7)
l1
[1, 2, 3, 4, [5, 6, 7, 8]]
l1+l2
[1, 2, 3, 4, [5, 6, 7, 8], 5, 6, 7, 8]
l1-l2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l1-l2
TypeError: unsupported operand type(s) for -: 'list' and 'list'
l1/l2
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l1/l2
TypeError: unsupported operand type(s) for /: 'list' and 'list'
l2.append(l1)
l2
[5, 6, 7, 8, [1, 2, 3, 4, [...]]]
l1
[1, 2, 3, 4, [5, 6, 7, 8, [...]]]
l1.remove
<built-in method remove of list object at 0x000002ABC200BF80>

l1.remove(l2)
l1
[1, 2, 3, 4]
t=(1,2,3,4)
t1=(5,6,7)
t.append(t1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.append(t1)
AttributeError: 'tuple' object has no attribute 'append'
t[3]
4
t[0]
1
t1[2]
7
l.reverse()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.reverse()
NameError: name 'l' is not defined. Did you mean: 'l1'?
l1.reverse()
l1
[4, 3, 2, 1]
l2.sort()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l2.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
t.sort()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
t+t1
(1, 2, 3, 4, 5, 6, 7)
t1
(5, 6, 7)
t.remove(6)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t.remove(6)
AttributeError: 'tuple' object has no attribute 'remove'
s1={1,2,3,4,5}
s1'
SyntaxError: unterminated string literal (detected at line 1)
s1
{1, 2, 3, 4, 5}
s1.reverse()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s1.reverse()
AttributeError: 'set' object has no attribute 'reverse'
s1.sort()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s1.sort()
AttributeError: 'set' object has no attribute 'sort'
t1.extend
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t1.extend
AttributeError: 'tuple' object has no attribute 'extend'
t1.extend(3)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t1.extend(3)
AttributeError: 'tuple' object has no attribute 'extend'
t.index()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t.index()
TypeError: index expected at least 1 argument, got 0
t.indedx(%)
SyntaxError: invalid syntax
t.index(2)
1
l3=[]
l3
[]
s1={}
s1
{}
t3=()
t3
()
type
<class 'type'>
(
type(s1)
<class 'dict'>
s=set{}
SyntaxError: invalid syntax
s=set()
type(s)
<class 'set'>
d=dict{}
SyntaxError: invalid syntax
d=dict()
d
{}
type(d)
<class 'dict'>
