def productExceptSelf(nums):#time complexity:O(n)
    out=[]
    n=len(nums)
    i=1
    j=n-2
    prifix=[1]*n
    sufix=[1]*n
    while i<n and j>=0:
        prifix[i]=prifix[i-1]*nums[i-1]
        i=i+1
        sufix[j]=sufix[j+1]*nums[j+1]
        j=j-1
    i=0
    j=n-1
    while i<n and j>=0:
        out.append(prifix[i]*sufix[i])
        i=i+1
        j=j-1
    return out

def productExceptSelf_optimal(nums):
    n=len(nums)
    out=[1]*(n)
    for i in range(1,n):
        out[i]=out[i-1]*nums[i-1]
    sufix=1
    for i in range(n-2,-1,-1):
        sufix*=nums[i+1]
        out[i]*=sufix
    return out

def setZeroes(matrix):
    zero=set()#SET
    m=len(matrix)#row
    n=len(matrix[0])#col
    for i in range(m):
        s=set(matrix[i])
        print(matrix[i])
        if 0 in s:
           zero.add(i)
    #create index
    #for row
    for i in range(n):
        if i in zero:
            matrix[i][:]=[0]*n
    #col
    j=0
    for row in matrix:
        for i in zero:
            row[i]=0
    print(zero)
    return matrix
matrix =[[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))
        