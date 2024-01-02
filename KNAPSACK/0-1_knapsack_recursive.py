arr = [1,3,4,5]
profit = [1,4,5,7]
weight = 7 

def knapsack_best(W,n):
    if W == 0 or n == 0:
        return 0 
    if arr[n-1] <= W:
        return max(profit[n - 1] + knapsack_best(W - arr[n-1], n - 1) , knapsack_best(W , n - 1))
    else:
        return knapsack_best(W , n - 1)

print(knapsack_best(7 , 4))