Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=input()
a
type(x)
<class 'str'>
print(x)
a
x=input()

type(x)
<class 'str'>
print(x)

x=int(input())

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x=int(input())
ValueError: invalid literal for int() with base 10: ''
x=int(input())
2
type(x)
<class 'int'>
x=input("Enter two values:").split()
Enter two values:2 3
type(x)
<class 'list'>
print(x)
['2', '3']
x=input("Enter two values:").split(',')
Enter two values:1 2
print(x)
['1 2']
type(x)
<class 'list'>
x=input("Enter two values:").split('A')
Enter two values:1 2
print(x)
['1 2']
x=input("Enter two values:").split('A')
Enter two values:1A2
print(x)
['1', '2']
x,y=input("Enter two values:").split()
Enter two values:1 2
print(x)
1
print(y)
2
type(x)
<class 'str'>
type(y)
<class 'str'>
x,y=int(input("Enter two values:")).split()
Enter two values:1 2
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x,y=int(input("Enter two values:")).split()
ValueError: invalid literal for int() with base 10: '1 2'
a,b = [int(x) for x in [10,20,30,40]]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a,b = [int(x) for x in [10,20,30,40]]
ValueError: too many values to unpack (expected 2)
a,b = [int(x) for x in [10,20,30,40].split()]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a,b = [int(x) for x in [10,20,30,40].split()]
AttributeError: 'list' object has no attribute 'split'
a,b = [int(x) for x in input("Enter 2 numbers:").split()]
Enter 2 numbers:2 3
print(a)
2
print(b)
3
a,b = [int(x) for x in input("Enter 3 numbers:").split()]
Enter 3 numbers:1 2 3 
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a,b = [int(x) for x in input("Enter 3 numbers:").split()]
ValueError: too many values to unpack (expected 2)
a,b = [int(x) for x in input("Enter 3 numbers:").split()]
Enter 3 numbers:1 2 3
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,b = [int(x) for x in input("Enter 3 numbers:").split()]
ValueError: too many values to unpack (expected 2)
x = eval("10,20,30")
print(x)
(10, 20, 30)
type(x)
<class 'tuple'>
x=input




x=input("enter the no")
enter the no10+20+30
y=eval(x)
print("The result is : ",y)
The result is :  60
