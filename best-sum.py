# O((n**m)*m)
# def best_sum(target_sum: int, numbers: list) -> list:
#     if target_sum == 0:
#         return []
#     if target_sum < 0:
#         return None
#     shortest_combination = None
#     for num in numbers:
#         remainder = target_sum - num
#         remainder_combination = best_sum(remainder, numbers)
#         if remainder_combination is not None:
#             remainder_combination.append(num)
#             combination = remainder_combination
#             if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
#                 shortest_combination = combination
#     return shortest_combination

# memoized O((m**2)*n)
def best_sum(target_sum: int, numbers: list):
    memo = {}
    return _best_sum(target_sum, numbers,memo)


def _best_sum(target_sum: int, numbers: list, memo: dict) -> list:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = _best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            remainder_combination = remainder_combination.copy()
            remainder_combination.append(num)
            combination = remainder_combination
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination


print(best_sum(7, [5, 2, 3, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [5, 3]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
