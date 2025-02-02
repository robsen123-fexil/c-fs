frst=input()
scnd=input()
f=''
s=''
for i in frst:
    f+=i.lower()
for i in scnd:
    s+=i.lower()




if s<f:
    print('1')
elif s>f:
    print('-1')
else:
    print('0')