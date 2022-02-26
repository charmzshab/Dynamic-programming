# O(n)
def fib(n):
    table = []
    for i in range(n+1):
        table.append(0)
    table[1] = 1
    for count in range(n):
        table[count+1] += table[count]
        if count < len(table)-2:
            table[count+2] += table[count]
    return table[n]