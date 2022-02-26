# O((m**2)*n)
def can_construct(target: str, words: list) -> bool:
    table = [False for i in range((len(target)+1))]
    table[0] = True
    for i in range(len(target)):
        if table[i]:
            for word in words:
                # if the word matches the characters starting at position i
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[len(target)]
