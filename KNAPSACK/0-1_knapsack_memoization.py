arr = [1,3,4,5]
profit = [1,4,5,7]
weight = 7 

# dimensions of this matrix depends on changing parameters in the recursive code like idx and W
dp = [ [0 ] * (weight + 1) for i in range(len(arr) + 1)]
print(dp)

def knapsack(ans , idx , W):    
    if idx == len(arr):
        return ans 
    if dp[idx][W] != 0:
        return dp[idx][W]
    
    if W >= arr[idx]: # possible h included 
        inc = knapsack(ans + profit[idx] , idx + 1 , W - arr[idx] )
    else: # not possible hence not included 
        inc = 0
    dp[idx][W ] =  max(ans , max(inc , knapsack(ans , idx + 1 , W ))) # doesn't matter if possible or not
    return dp[idx][W]
print(knapsack(0,0,7))