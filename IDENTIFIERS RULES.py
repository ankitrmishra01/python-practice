Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A=10
A
10
a=10
a
10
id(A)
1441064354320
id(a)
1441064354320
1A=10
SyntaxError: invalid decimal literal
A12=20
A12
20
id(A12)
1441064354640
aaaaaaaabbbb=20
aaaaaaaabbbb
20
x=30
x
30
_x=30
_x
30
__x=20
__x
20
x=True
x
True
y=False
y
False
x+y=True
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
x+y==True
True
A=10
type(A)
<class 'int'>
a='''How are you"@"bro'''
a
'How are you"@"bro'
b="where are you?"
b
'where are you?'
print(a)
How are you"@"bro
print(b)
where are you?
x*y==False
True
a="adityapatelpu'''is bad boy'''pu"
a
"adityapatelpu'''is bad boy'''pu"
print(a)
adityapatelpu'''is bad boy'''pu
c='whatareyoudoing "yash" in one piece'
c
'whatareyoudoing "yash" in one piece'
print(c)
whatareyoudoing "yash" in one piece
p='''parul"patel"'''
p
'parul"patel"'
print(p)
parul"patel"
e='''"A"'''
print(e)
"A"
A
10
B
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    B
NameError: name 'B' is not defined. Did you mean: 'b'?
a
"adityapatelpu'''is bad boy'''pu"
p
'parul"patel"'
c
'whatareyoudoing "yash" in one piece'
A12
20
a=print(int(20.5))
20
int(10+3j)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(10+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(int(10+3j))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(int(10+3j))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
a=20
str(A)
'10'
bool(A)
True
print(int(a))
20
print(int(p))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(int(p))
ValueError: invalid literal for int() with base 10: 'parul"patel"'
print(int('123'))
123
print(int("12.5"))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(int("12.5"))
ValueError: invalid literal for int() with base 10: '12.5'
//how many type of errors in python....
SyntaxError: invalid syntax
int()
0
bool()
False
str()
''
float()
0.0
complex(A)
(10+0j)
complex()
0j
