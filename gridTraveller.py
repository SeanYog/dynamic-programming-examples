def gridTraveller_memo(m, n, memo=None):
    if isinstance(memo, type(None)):
        memo = {}
    
    key = (m,n)
    
    if key in memo: return memo[key]
    
    if m == 1 and n == 1: return 1
    
    if m == 0 or n == 0: return 0
    
    memo[key] = gridTraveller_memo(m-1, n, memo) + gridTraveller_memo(m, n-1, memo)
    return memo[key]




print(gridTraveller_memo(2,3))
print(gridTraveller_memo(3,1))
print(gridTraveller_memo(1,3))
print(gridTraveller_memo(18,17))
