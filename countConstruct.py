# O((n**m)*m)
# def count_construct(target: str, word_bank: list) -> int:
#     if target == '':
#         return 1
#     total_count = 0
#     for word in word_bank:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             total_count += count_construct(suffix, word_bank)
#     return total_count

def count_construct(target: str, word_bank: list):
    memo = {}
    return _count_construct(target, word_bank,memo)

def _count_construct(target: str, word_bank: list, memo: dict) -> int:
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            total_count += _count_construct(suffix, word_bank, memo)
    memo[target] = total_count
    return total_count




print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
    ]))  # 0