t=int(input())
for _ in range(t):
    n  , x= map(int  , input().split())
    lists=list(map(int , input().split()))
    res=[]
    for i in range(x+1):
        res.append(i)
    
    maxima=(abs(max(lists)-res[-1])) *2
    
    result=[]
    result.append(maxima)
    result.append(min(lists))
    
    for i in range(1 ,len(lists)):
        result.append(lists[i]-lists[i-1])
    print(max(result))