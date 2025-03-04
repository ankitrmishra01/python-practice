Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=0
bool(a)
False
float(15)== 15.0
True
float(0B1111)== 15.0
True
float(20+3j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    float(20+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True) == 1.0
True
float(False) == 0.0
True
float('10.5')==>10.5
SyntaxError: invalid syntax
float('20')==>10
SyntaxError: invalid syntax
float9
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float9
NameError: name 'float9' is not defined. Did you mean: 'float'?
float('10')
10.0
float('10.5')
10.5
float(True)
1.0
float(False)
0.0
float(15)
15.0
float(0B11111)
31.0
float
<class 'float'>
(
float(10+0j)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float(10+0j)
TypeError: float() argument must be a string or a real number, not 'complex'
float
<class 'float'>
(
float('abc')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float('abc')
ValueError: could not convert string to float: 'abc'
complex(10)
(10+0j)
complex('a',3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    complex('a',3)
TypeError: complex() can't take second arg if first is a string
complex('a','b')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex('a','b')
TypeError: complex() can't take second arg if first is a string
complex(1,2)
(1+2j)
complex(True)
(1+0j)
complex(False)
0j
complex(True,False)
(1+0j)
complex(False,False)
0j
complex(True,2)
(1+2j)
bool(!)
SyntaxError: invalid syntax
bool(1)
True
bool(0)
False
bool(10.5)
True
bool(10+2j)
True
bool(0+0j)
False
bool('a')
True
bool('')
False
bool(None)
False
type(print())

<class 'NoneType'>
type(print(yash ))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    type(print(yash ))
NameError: name 'yash' is not defined. Did you mean: 'hash'?
type(print("yash"))
yash
<class 'NoneType'>
bool(' ')
True
str('10.5)
    
SyntaxError: unterminated string literal (detected at line 1)
str('10.5')
    
'10.5'
str(10.5)
    
'10.5'
str('abcd')
    
'abcd'
str(True)
    
'True'
str(None)
    
'None'
str('10+0j')
    
'10+0j'
str
    
<class 'str'>
str(0b1111111)
    
'127'
str(False)
    
'False'
str('adityabadboy')
    
'adityabadboy'
a=('hello world')
    
a='hello world'
    
len(a)
    
11
len(a[2:4])
    
2
a[2:3]
    
'l'
a[2:10]
    
'llo worl'
str()
    
''
reversed(a)
    
<reversed object at 0x0000016E929B7DC0>
reversed('a')
    
<reversed object at 0x0000016E929B6E00>
print(reversed(a))
    
<reversed object at 0x0000016E929B6DA0>
a[::-3]
    
'dooe'
slice(a)
    
slice(None, 'hello world', None)
slice(a, 7)
    
slice('hello world', 7, None)
slice(a, 9 , 9)
    
slice('hello world', 9, 9)
a[0:2:5]
    
'h'
str
    
<class 'str'>
9
str(2+3j)
    
'(2+3j)'
str(['red','green','blue'])
    
"['red', 'green', 'blue']"
a='Hello'
    
a.lower()
    
'hello'
a.upper()
    
'HELLO'
d.strip()
    
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d.strip()
NameError: name 'd' is not defined. Did you mean: 'id'?
a='  Book '
    
a.strip()
    
'Book'
a='9999'
    
a
a.digit()
    
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.digit()
AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
a.isdigit()
    
True

