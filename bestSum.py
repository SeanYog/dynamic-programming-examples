'''
Like howSum but returns the shortest answer
m = targetSum
n = len(numbers)

Complexity:
base:
Time: O((n^m) * m) Space: O(m^2)
memo:
Time: O() Space: O()
'''


def bestSum(targetSum, numbers, memo=None):
    if isinstance(memo, type(None)):
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0: 
        return []
    if targetSum < 0: 
        return None

    best = None

    for num in numbers:
        reminder = targetSum-num
        res = bestSum(reminder, numbers, memo)
        
        if res is not None:
            # combi = res.copy()
            # combi.append(num)
            combi = res + [num]
            if best is None or len(combi) < len(best):
                best = combi
    
    memo[targetSum] = best
    return best
    
        
        

print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))
