Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello"+"hii")
hellohii
a, b, c=10, 20, 30
print(a, b, c)
10 20 30
print(a, b, c, sep=',')
10,20,30
print("hello" end = '')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("hello", end = '')
hello
print("hii", end= " ")
hii 
print("ok", end= '...')
ok...
print(10,20,30,40,sep = ':')
10:20:30:40
name="Ankit"
l=[85,84,86]
print("hello %s the list is: %s",%(name,l))
SyntaxError: invalid syntax
print("hello %s the list is: %s"%(name,l))
hello Ankit the list is: [85, 84, 86]
name="Ankit"
salary="1000000000000000"
add="Silvassa"
print("hello{0} your salary is{1} and your add {2}".format(name,salary,add))
helloAnkit your salary is1000000000000000 and your add Silvassa
print("hello {0} your salary is {1} and your add {2}".format(name,salary,add))
hello Ankit your salary is 1000000000000000 and your add Silvassa
print("priority always goes to local")
priority always goes to local
print("hello {} your salary is {} and your add {}".format(name,salary,add))
hello Ankit your salary is 1000000000000000 and your add Silvassa
f"The number is {21}"
'The number is 21'
a=5
b=10
f"{a} plus {b} is {a+b}"
'5 plus 10 is 15'
debit= 300
credit=500
f"{Debit: ${debit}, Credit: ${credit}, Balance: ${credit-debit}"
SyntaxError: f-string: expecting '}'
