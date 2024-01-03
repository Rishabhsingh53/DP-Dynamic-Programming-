arr = [1,3,4,5]
profit = [1,4,5,7]
weight = 7 

# dimensions of this matrix depends on changing parameters in the recursive code like idx and W
dp = [ [0 ] * (weight + 1) for i in range(len(arr) + 1)]


def knapsack(W,n):
    if W == 0 or n == 0:
        return 0 
    if dp[n][W] != 0:
        return dp[n][W]
    if arr[n-1] <= W:
        dp[n][W] = max(profit[n - 1] + knapsack(W - arr[n-1], n - 1) , knapsack(W , n - 1))
    else:
        dp[n][W] =  knapsack(W , n - 1)
    return dp[n][W]

print(knapsack(weight, 4))