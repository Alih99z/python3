
from msilib.schema import Binary
binary=[]
x1 = int(input("Enter the decimai number :"))
x2 = x1
while x2!=0:
    x3=x2%2
    binary.append(x3)
    x2=x2//2
binary.reverse()
x4=" "
for i in binary:
    x4=x4+str(i)
print("Decimil :",x1,"<===>","binary :",x4)


