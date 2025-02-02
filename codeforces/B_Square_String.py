t= int(input())
for i in range(t):
    strs=input()
    leng=len(strs)
    if leng%2!=0:
        print('NO')
    else:
        middles=leng//2
        if strs[middles:]==strs[:middles]:
            print('YES')
        else:
            print('NO')
            
