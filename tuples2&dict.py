Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=(1,2,3)
a
(1, 2, 3)
l=[1,2,3,4]
l
[1, 2, 3, 4]
l1=[1,2,3]
l1+l
[1, 2, 3, 1, 2, 3, 4]
l1.appendl
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l1.appendl
AttributeError: 'list' object has no attribute 'appendl'. Did you mean: 'append'?
l.appendl1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l.appendl1
AttributeError: 'list' object has no attribute 'appendl1'. Did you mean: 'append'?
t=(10)
t
10
print(t)
10
type(10)
<class 'int'>
type(t)
<class 'int'>
t1=(1,2,3)
t1+t
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t1+t
TypeError: can only concatenate tuple (not "int") to tuple
t.append(t1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t.append(t1)
AttributeError: 'int' object has no attribute 'append'
t=(10,)
r
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    r
NameError: name 'r' is not defined
t
(10,)
print(t)
(10,)
type(t)
<class 'tuple'>
t=10,
t
(10,)
type(t)
<class 'tuple'>
print(t)
(10,)
d={a,'1';b,'2'}
SyntaxError: invalid syntax
d={a:1,b:2}
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d={a:1,b:2}
NameError: name 'b' is not defined
d={a:1}
d
{(1, 2, 3): 1}
d={ankit:100,ayush:50}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d={ankit:100,ayush:50}
NameError: name 'ankit' is not defined. Did you mean: 'anext'?
a
(1, 2, 3)
b
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b
NameError: name 'b' is not defined
b=20
c=30
d={a:1,b:2,c:3}
d
{(1, 2, 3): 1, 20: 2, 30: 3}
d={a:1,b:2,c:3,a=2,3,4}
SyntaxError: ':' expected after dictionary key
d={k1:v1,k2:v2,k3:v3,k1=v2,v3,v4}
SyntaxError: ':' expected after dictionary key
d={k1:v1,k2:v2,k3:v3,k1:v2,v3,v4}
SyntaxError: ':' expected after dictionary key
print(d)
{(1, 2, 3): 1, 20: 2, 30: 3}
type(d)
<class 'dict'>
a=ankit
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a=ankit
NameError: name 'ankit' is not defined. Did you mean: 'anext'?
a='ankit'
b='bhavee'
d={a:100,b:1}
d
{'ankit': 100, 'bhavee': 1}
d={'a':[10,20,30,(40,50,60),'b':'c','d','e'}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d={'a':[10,20,30,(40,50,60)],'b':'c','d','e'}
   
SyntaxError: ':' expected after dictionary key
d={'a':[10,20,30,(40,50,60)],'b','c','d','e'}
   
SyntaxError: ':' expected after dictionary key
d={'a':[10,20,30,(40,50,60)],'b':['c','d','e
                                  
SyntaxError: unterminated string literal (detected at line 1)
d={'a':[10,20,30,(40,50,60)],'b':['c','d','e']}
                                  
d
                                  
{'a': [10, 20, 30, (40, 50, 60)], 'b': ['c', 'd', 'e']}
print(60)
                                  
60
d
                                  
{'a': [10, 20, 30, (40, 50, 60)], 'b': ['c', 'd', 'e']}
d[:2]
                                  
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    d[:2]
TypeError: unhashable type: 'slice'
d[2]
                                  
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d[2]
KeyError: 2
d[1]
                                  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d[1]
KeyError: 1
d['a'][-1][-1]
                                  
60
d['b'][2]
                                  
'e'
d['a'][0][3]
                                  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d['a'][0][3]
TypeError: 'int' object is not subscriptable
d['a'][0][1]
                                  
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d['a'][0][1]
TypeError: 'int' object is not subscriptable
KeyboardInterrupt
d['a'][0]
                                  
10
d['a'][3][2]
                                  
60
d['a'][2]
                                  
30
d={'k1':10,'k2':20}
                                  
d
                                  
{'k1': 10, 'k2': 20}
type(k2)
                                  
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    type(k2)
NameError: name 'k2' is not defined
type(k1)
                                  
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    type(k1)
NameError: name 'k1' is not defined. Did you mean: 'l1'?
type(d[k1])
                                  
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    type(d[k1])
NameError: name 'k1' is not defined. Did you mean: 'l1'?
type(d['k1'])
                                  
<class 'int'>
d={'k1':(10,20),'k2':20}
                                  
type(d['k1'])
                                  
<class 'tuple'>
d={'k1':[10,20],'k2':20}
                                  
type(d['k1'])
                                  
<class 'list'>
s='ankit'
                                  
s[0:2]
                                  
'an'
s[0:2:1]
                                  
'an'
s[0].upper+s[1:]
                                  
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s[0].upper+s[1:]
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'str'
s[0].upper+s[3:]
                                  
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s[0].upper+s[3:]
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'str'
s[0].upper+s.s[2:]
                                  
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s[0].upper+s.s[2:]
AttributeError: 'str' object has no attribute 's'
s[0].upper+s.s[1:-2]
                                  
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s[0].upper+s.s[1:-2]
AttributeError: 'str' object has no attribute 's'
s[0].upper()+s[1:]
                                  
'Ankit'
s='good'+10
                                  
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s='good'+10
TypeError: can only concatenate str (not "int") to str
s='good'+str(10)
                                  
s
                                  
'good10'
s='a'+'b'
                                  
s
                                  
'ab'
a
                                  
'ankit'
a='abv'*3
                                  
a
                                  
'abvabvabv'
def show():
    print(a)
show()
SyntaxError: invalid syntax
for i in range(0,10):
    i++
    
SyntaxError: invalid syntax
range(a)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    range(a)
TypeError: 'str' object cannot be interpreted as an integer
for i in range(0)
SyntaxError: expected ':'

= RESTART: C:/Users/ankit/OneDrive/Documents/SEMESTER 4/PYTHON/PYTHON PRACTICE/for loop.py
0
1
2
3
4
5
6
7
8
9

= RESTART: C:/Users/ankit/OneDrive/Documents/SEMESTER 4/PYTHON/PYTHON PRACTICE/for loop.py
0
1
2
3
4
5
6
7
8
9

= RESTART: C:/Users/ankit/OneDrive/Documents/SEMESTER 4/PYTHON/PYTHON PRACTICE/for loop.py
0
2
4
6
8

= RESTART: C:/Users/ankit/OneDrive/Documents/SEMESTER 4/PYTHON/PYTHON PRACTICE/for loop.py
P
Traceback (most recent call last):
  File "C:/Users/ankit/OneDrive/Documents/SEMESTER 4/PYTHON/PYTHON PRACTICE/for loop.py", line 3, in <module>
    print(i[1])
IndexError: string index out of range
