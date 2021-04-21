def fibonachi_memo(n, memo=None):
    if isinstance(memo, type(None)):
        memo = {}
        
    if n in memo: return memo[n]

    if n <= 2: return 1

    memo[n] = fibonachi_memo(n-1, memo) + fibonachi_memo(n-2, memo)
    return memo[n]



print(fibonachi_memo(5))
print(fibonachi_memo(10))
print(fibonachi_memo(13))
print(fibonachi_memo(50))
print(fibonachi_memo(100))
