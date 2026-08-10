import math

def merge(array,start,mid,end):
    temp=[]
    i=start#itorator for left
    j=mid+1#itorator for right
    #merging
    while(i<=mid and j<=end):
        if array[i]<=array[j]:
            temp.append(array[i])
            i=i+1
        else:
            temp.append(array[j])
            j=j+1
            
    #for remainig left elements
    while i<=mid:
        temp.append(array[i])
        i=i+1
    #for remainig right elements
    while j<=end:
        temp.append(array[j])
        j=j+1
    #copy temp into original
    for i in range(len(temp)):
        array[i+start]=temp[i]
def margeSort(array,start,end):
    if start<end:
        mid=(start+end)//2
        #left half
        margeSort(array,start,mid)
        #right half
        margeSort(array,mid+1,end)
        #merge
        merge(array,start,mid,end)

def merge_arr(num1,m,num2,n):#O(nlogn)
    idx=m+n-1
    i=m-1
    j=n-1
    while(i>=0 and j>=0):
        if num1[i]<=num2[j]:
            num1[idx]=num2[j]
            j=j-1
        else:
            num1[idx]=num1[i]
            i=i-1
        idx=idx-1
    
    while j>=0:
        num1[idx]=num2[j]
        idx=idx-1
        j=j-1
    
def singleNumber(nums):#O(NlogN) my logic
    nums.sort()
    privious=None
    count=1
    for i in nums:
        if privious==i:
            count=count+1
        else:
            count=count-1
        if count<0:
            return privious
        privious=i
    return privious
def singalNumberXOR(nums):#O(n) perfect
    ans=0
    for i in nums:
        ans^=i
    return ans
