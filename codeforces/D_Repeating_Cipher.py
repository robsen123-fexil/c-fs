n=int(input())-1
t=input()
ans=""
k=1
i=0
k=0
while k<n:
    ans+=t[k]
    i+=1
    k+=(i+1)
print(ans+t[-1])
    
