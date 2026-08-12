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
height = [1,8,6,2,5,4,8,3,7]
print(maxArea_optimal(height))