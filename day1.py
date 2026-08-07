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

a=[4,3,4,4,3,7]
print(majority_element_moores_voting_algo(a))