# Gets a targetSum and returns True/False if it can be computed from the numbers array

def canSum(targetSum, numbers):
    if targetSum == 0: 
        return True

    if targetSum < 0: 
        return False

    for num in numbers:
        if canSum(targetSum - num, numbers) == True: 
            return True
    
    return False


def canSum_memo(targetSum, numbers, memo=None):
    if isinstance(memo, type(None)):
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0: 
        return True

    if targetSum < 0: 
        return False

    for num in numbers:
        remains = targetSum - num
        if canSum_memo(remains, numbers, memo) == True: 
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False




print(canSum_memo(7, [2, 3])) # true
print(canSum_memo(7, [5, 3, 4, 7])) # true
print(canSum_memo(7, [2, 4])) # false
print(canSum_memo(8, [2, 3, 5])) # true
print(canSum_memo(300, [7, 14])) # false
