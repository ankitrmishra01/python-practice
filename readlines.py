f=open('abc.txt',mode = 'r')
data=f.readlines()
print(data)
f.close()
print(type(data))
