n=int(input())
for i in range(n):
    strs=input()
    if len(strs)<=10:
        print(strs)
    else:
        print(strs[0]+str(len(strs)-2)+strs[-1])


