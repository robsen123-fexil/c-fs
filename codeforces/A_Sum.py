t=int(input())
def checker(nums):
    for j in range(len(nums)):
        for k in range(len(nums)):
            frst=nums[j]+nums[k]
            if frst in nums:
                return 'YES'
    return 'NO'              
    


for i in range(t):
    a , b , c= (map(int , input().split()))
    if a==b+c or b==c+a or c==a+b:
        print('YES')
    else:
        print('NO')
     


