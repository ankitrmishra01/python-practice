with open('abc.txt',mode='r') as f:
    data1=f.readlines()
    count=int(input("enter no of rows you want to print:"))
    for line in data1[0:count]:
        print(line,end='')
    print("close file:",f.closed)
print("close file:",f.closed)
