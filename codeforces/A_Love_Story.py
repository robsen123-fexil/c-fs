t=int(input())
for i in range(t):
    strs=input()
    cnt=0
    for a , b in zip(strs , 'codeforces'):
        if a!=b:
            cnt+=1
    print(cnt)