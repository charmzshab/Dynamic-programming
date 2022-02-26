# O(n**m)
# def all_construct(target: str, word_bank: list) -> list:
#     if target == '':
#         return [[]]
#     result = []
#     for word in word_bank:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             suffix_ways = all_construct(suffix, word_bank)
#             target_ways = [el[:] for el in suffix_ways]
#             [el.insert(0, word) for el in target_ways]
#             result.extend(target_ways)
#     return result

# memoized O(n**m)
def all_construct(target: str, word_bank: list):
    memo = {}
    return _all_construct(target, word_bank, memo)

def _all_construct(target: str, word_bank: list, memo) -> list:
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = _all_construct(suffix, word_bank, memo)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            # ret_target = [el[:] for el in target_ways]
            result.extend(target_ways)
    memo[target] = result
    return result


print(all_construct('hello', ['cat', 'dog', 'mouse']))  # []
print(all_construct('', ['cat', 'dog', 'mouse']))  # [[]]
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # [['le', 'purp'], ['le', 'p', 'ur', 'p']]
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))  # [['ef', 'cd', 'ab'], ['def', 'c', 'ab'], ['def', 'abc'], ['ef', 'abcd']]
