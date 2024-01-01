arr = [1,3,4,5]
profit = [1,4,5,7]
weight = 7 

def knapsack(ans , idx , W):    
    if idx == len(arr):
        return ans 
    
    if W >= arr[idx]: # possible h included 
        inc = knapsack(ans + profit[idx] , idx + 1 , W - arr[idx] )
    else: # not possible hence not included 
        inc = 0
    return max(ans , max(inc , knapsack(ans , idx + 1 , W ))) # doesn't matter if possible or not

print(knapsack(0,0,7))