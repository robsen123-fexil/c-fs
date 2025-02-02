t=int(input())
result=[]
result=list(map(int , input().split()))
maxima=float('-inf')
summ=sum(result)
if sum(result)%2==0:
    maxima=max(maxima ,sum(result))
    print(maxima)
else:
    for i in range(len(result)):
        if (summ-result[i])%2==0:
            maxima=max(maxima ,(summ-result[i]) )
    print(maxima)            
