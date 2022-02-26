# Problem: write a function fib(n) that takes in a number as an argument. 
# The function should return the n-th number of the Fibonacci sequence. The 0th number of the sequence is 0.
#  The 1st number of the sequence is 1. To generate the next number of the sequence, we sum the previous two.


# O(2**n)
# def fib(n: int) -> int:
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)


# memoization O(n)
def fib(n: int, memo={}) -> int:
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]




print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025