# The base condition from recursive function is changed to intialization in DP

wt = [1, 3, 4 ,5 ]
val = [ 1 ,4, 5 ,7]
W = 7 

def knapsack_dp(W , n ):
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(len(wt) + 1) ]
    # n = i and W = j 
    
    for i in range(1,n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i  - 1][j]
    return (dp[-1][-1])
knapsack_dp(W , 4)