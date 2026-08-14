def largestSum(nums):
    cs=0
    ms=float("-inf")
    for i in range(len(nums)):
        cs+=nums[i]
        ms=max(cs,ms)
        if cs<0:
            cs=0
    return ms

def maxArea(heights):
    #brutforce
    n=len(heights)
    maxWater=0
    for i in range(n):
        for j in range(i+1,n):
            width=j-i
            hight=min(heights[i],heights[j])
            area=width*hight
            maxWater=max(maxWater,area)
            #move pointer
            
    return maxWater
def maxArea_optimal(height):
    i=0
    j=len(height)-1
    maxWater=0
    while i<j:
        hight=min(height[i],height[j])
        width=j-i
        area=hight*width
        maxWater=max(maxWater,area)
        if height[i]<height[j]:
            i=i+1
        else:
            j=j-1
    return maxWater
#sort colors
def sortColors(nums):
    #MYLOGIC
    n=len(nums)
    for i in range(n):
        for j  in range(i+1,n):
            temp=i
            if nums[i]>=nums[j]:
                temp=j
            nums[i],nums[temp]=nums[temp],nums[i]
           ## print(nums)
    return nums
def sortColors_optimal(nums):#O(n)
    count0=0
    count1=0
    count2=0
    for i in nums:
        if i==0:
            count0+=1
        elif i==1:
            count1+=1
        else:
            count2+=1
    #sort
    idx=0
    for i in range(count0):
        nums[idx]=0
        idx+=1
    for i in range(count1):
        nums[idx]=1
        idx+=1
    for i in range(count2):
        nums[idx]=2
        idx+=1
    return nums

def threeSum(nums):
    out=[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    out.append([nums[i],nums[j],nums[k]])
    return out
def threeSum_optimize(nums):
    nums.sort()
    out=[]
    n=len(nums)
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            Sum=nums[i]+nums[j]+nums[k]
            if Sum<0:
                j=j+1
            elif Sum>0:
                k=k-1
            else:
                out.append([nums[i],nums[j],nums[k]])
                j=j+1
                k=k-1
                while j<k and nums[j]==nums[j-1]:
                    j=j+1
    return out

def fourSum(nums,target):#O(nlogn+n^3)
    out=[]
    n=len(nums)
    nums.sort()
    for a in range(n):
        if nums[a]==nums[a-1] and a>0:
            continue
        b=a+1
        while b<n:
            c=b+1
            d=n-1
            while c<d:
                Sum=nums[a]+nums[b]+nums[c]+nums[d]
                if Sum<target:
                    c=c+1
                elif Sum>target:
                    d=d-1
                else:
                    out.append([nums[a],nums[b],nums[c],nums[d]])
                    c=c+1
                    d=d-1
                    while c<d and nums[c]==nums[c-1]:
                        c=c+1
            b=b+1
            while(b<n and nums[b]==nums[b-1]):
                b=b+1
    return out
nums =[-2,-1,-1,1,1,2,2]
print(fourSum(nums,0))