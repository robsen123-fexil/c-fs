leng=int(input())
for i in range(leng):
    strs=input()
    if len(strs)<10:
        print(strs)
    else:
        print(strs[0]+str(len(strs)-2)+strs[-1])
        