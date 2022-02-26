# O((m**2)*n)
def count_construct(target: str, words: list) -> int:
    table = [0 for i in range(len(target)+1)]
    table[0] = 1
    for i in range(len(target)):
        for word in words:
            if word == target[i:(i + len(word))]:
                table[i+len(word)] += table[i]
    return table[len(target)]