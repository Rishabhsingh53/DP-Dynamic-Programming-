# return the total number of ways such that the sum of coins is total. We can use a coin any number of times

coins = [1, 2 , 3]
total = 5 

# RECURSIVE 
def coin_change(curr , total , coins, n ):
    if curr == total:
        return 1 
    
    if curr > total or n == 0:
        return 0 
    
    return coin_change(curr + coins[n-1] , total , coins , n ) + coin_change(curr , total, coins, n - 1 )
 
print(coin_change(0 , total , coins , len(coins)))

