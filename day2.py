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
arr=[[9,1,7],[8,9,2],[3,4,6]]
print(missing_value_sorting_aproch(arr))
            