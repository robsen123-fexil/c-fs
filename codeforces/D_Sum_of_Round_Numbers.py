t=int(input())
cnt=0
for i in range(t):
    n=int(input())
    strs=str(n)
    res=[]
    for i in range(len(strs)):
        s=strs[i]
        if int(strs[i])!=0:
            l=i+1
            while l<len(strs) and  int(strs[l])==0:
                s+=strs[l]
                l+=1
        if int(s)!=0:
            res.append(s)
    print(len(res))
    
        

    



    

