s=input()
arr=s.split(",")
z=""
x=arr.index('5')
y=arr.index('8')
s=0
for i in range(len(arr)):
    if(i>=x and i<=y):
        z+=arr[i]
    else:
        s+=int(arr[i])
print(s+int(z))