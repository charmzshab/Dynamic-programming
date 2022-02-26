# O(n*m)
def can_sum(target_sum: int, numbers: list) -> bool:
    table = []
    [table.append(False) for i in range(target_sum+1)]
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for num in numbers:
                if (i+num) <= target_sum:
                    table[i+num] = True
    return table[target_sum]
