f=open('abc.txt',mode='r')
data1=f.readlines()
line_no=int(input("enter no of rows which you want to read"))
for line in data1[0:line_no]:
    print(line,end='')
f.close()
