# O((m**2)*n)
def how_sum(target_sum: int, numbers: list) -> list:
    table = [None for i in range(target_sum+1)]
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for k in numbers:
                if (i+k) <= target_sum:
                    table[i+k] = table[i].copy()
                    table[i+k].append(k)
    return table[target_sum]