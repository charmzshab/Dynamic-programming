# O((m**2)*n)
def best_sum(target_sum: int, numbers: list) -> list:
    table = [None for i in range(target_sum+1)]
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if (i+num) <= target_sum:
                    candidate = table[i].copy()
                    candidate.append(num)
                    if table[i+num] is None or (len(table[i+num]) > len(candidate)):
                        table[i+num] = candidate
    return table[target_sum]
