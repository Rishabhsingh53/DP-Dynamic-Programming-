arr = [2 , 4 ,5, 7, 8, 5]
sum = 100

def recursive(curr, n):
    
    if curr == sum:
        return True 
    if n < 1:
        return False 
    
    if arr[n-1] <= sum:
        return recursive(curr + arr[n-1] , n - 1) or recursive(curr , n - 1)
    else:
        return recursive(curr , n -1 )
    
print(recursive(0 , 6))


def subset_sum(sum , n ):
    n = len(arr)
    dp = [[0] * (sum + 1) for _ in range(len(arr) + 1) ]

    for i in range(len(arr)):
        dp[i][0] = True 
    for j in range(1, sum + 1):
        dp[0][j] = False
        
    for i in range(1,n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = ( dp[i-1][j - arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] = dp[i  - 1][j]
    return (dp[-1][-1])
# print(subset_sum(sum, N))
