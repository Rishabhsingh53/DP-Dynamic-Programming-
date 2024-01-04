arr = [1, 1 ,1 ,1 ,1 ]
target = 3 
# RECURSION -- TLE 
def targetSum(target , curr , n): 
    
    if n == 0 and curr == target:
        return 1
    elif n == 0 and curr != target:
        return 0
    
    return targetSum(target , curr + arr[n - 1] , n - 1) + targetSum(target , curr - arr[n-1] , n - 1)

# MEMOIZATION -- ACCEPTED 

# DP -- ACCEPTED 

print(targetSum(target, 0 , len(arr)))