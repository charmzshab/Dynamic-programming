# brute force O(n**m)
# def can_sum(target_sum: int, numbers: list) -> bool:
#     if target_sum == 0:
#         return True
#     if target_sum < 0:
#         return False
#     for num in numbers:
#         remainder = target_sum - num
#         if can_sum(remainder, numbers):
#             return True
#     return False

# memoization O(m*n)
def can_sum(target_sum: int, numbers: list):
    memo = {}
    return _can_sum(target_sum, numbers,memo)


def _can_sum(target_sum: int, numbers: list,memo) -> bool:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if _can_sum(remainder, numbers,memo):
            memo[target_sum] = True
            return memo[target_sum]
    memo[target_sum] = False
    return memo[target_sum]

print(can_sum(7,[2,3]))
print(can_sum(7,[5,3,4,7]))
print(can_sum(7,[2,4]))
print(can_sum(8,[2,3,5]))
print(can_sum(300,[7,14]))