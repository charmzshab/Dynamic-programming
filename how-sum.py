# O((n**m)*m) Bruteforce
# def how_sum(target_sum: int, numbers: list) -> list:
#     if target_sum == 0:
#         return []
#     if target_sum < 0:
#         return None
#     for num in numbers:
#         remainder = target_sum - num
#         remainder_res = how_sum(remainder, numbers)
#         if remainder_res is not None:
#             remainder_res.append(num)
#             # [*remainder_res,num]
#             return remainder_res
#     return None


# memoized O((m**2)*n)
def how_sum(target_sum: int, numbers: list):
    memo = {}
    return _how_sum(target_sum, numbers,memo)

def _how_sum(target_sum: int, numbers: list,memo) -> list:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_res = _how_sum(remainder, numbers,memo)
        if remainder_res is not None:
            remainder_res.append(num)
            # [*remainder_res,num]
            memo[target_sum] = remainder_res
            return memo[target_sum]
    memo[target_sum] = None
    return memo[target_sum]

print(how_sum(7, [2, 3]))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # None