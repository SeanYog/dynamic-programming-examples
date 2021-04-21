'''

Gets a targetSum number and an array of numbers.
Returns whether the targetSum can be computerd from the numbers array and how
If it cants - returns None

Complexity
m is the target sum
n is the length of the numbers array
without memo: 
time: O((n^m)*m), space: O(m)

with memo:
time: O(n*(m^2)), space: O(m^2)
'''


def howSum(targetSum, numbers, memo=None):
    if isinstance(memo, type(None)):
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        remain = targetSum - num
        res = howSum(remain, numbers, memo)
    
        if res is not None:
            res.append(num)
            memo[targetSum] = res
            return res
    
    memo[targetSum] = None
    return None


print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7, 14]))
    
