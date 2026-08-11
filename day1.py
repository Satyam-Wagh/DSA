#pair sum
def Pair_sum_brute_force(array,target):#O(n^2) brute force approch
    n=len(array)
    for i in range(n):
        for j in range(i+1,n):
            if (array[i]+array[j])==target:
                return (array[i],array[j])
    return "Theire is no numbers found.."

def Pair_sum_optimal(arr,target):#O(n)optimal
    n=len(arr)    
    i=0
    j=n-1
    pair_sum=0
    while i<j:
        pair_sum=arr[i]+arr[j]
        if pair_sum>target:
            j=j-1
        elif pair_sum<target:
            i=i+1
        else:
            return (arr[i],arr[j])
    return "Not found"

#majority element
def majority_element_brute_force(arr):#O(n^2)
    n=len(arr)
    for i in arr:
        frequency=0
        for j in arr:
            if i==j:
               frequency=frequency+1
        if frequency>int(n/2):
            return i
        
def  majority_element_optimal(arr):#O(nlogn)
    arr.sort()#O(nlogn)
    n=len(arr)
    frq=1
    ans=arr[0]
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            frq=frq+1
        else:
            frq=1
            ans=arr[i]
        if frq>int(n/2):
            return arr[i]
        
def majority_element_moores_voting_algo(arr):#O(n) most recommended
    frq=0
    ans=0
    for i in arr:
        if frq==0:
            ans=i
        frq=frq+1 if ans==i else frq-1
        print(f"at {i} frq={frq} and ans={ans}")
    return ans

#repeating and missing value
def missing_value(arr):
    n=len(arr)#calculate length
    visited={i:False for i in range(1,(n*n)+1)}
    flat_arr=[item for i in arr for item in i] #[[],[]]=>[]
    repate=0
    miss=0
    #Find reapate value
    for i in flat_arr:
        if not visited[i]:
            visited[i]=True
        else:#already visited
            repate=i
    #find missing value
    for i in visited:
        if not visited[i]:
            miss=i
            break
    return [repate,miss]
def missing_value_sorting_aproch(grid):
    n=len(grid)
    sq=n*n
    sets=set()
    expected_sum=(sq*(sq+1))/2
    actual_sum=0
    repeat=0
    #find the repeating value
    for i in grid:
        for j in i:
            if j in sets:
                repeat=j
            else:
                sets.add(j)
            actual_sum+=j
    #find missing value
    miss=expected_sum+repeat-actual_sum
    return [repeat,miss]

#merging 2 sorted array
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
        
#single number
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

#stock by and sell
def StockBuyOrSell(prices):#O(n)
    mp=0#max profit
    bestBuy=prices[0]
    for i in range(len(prices)):
        if prices[i]>bestBuy:
            mp=max(mp,prices[i]-bestBuy)
        bestBuy=min(bestBuy,prices[i])
    return mp