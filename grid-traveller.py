# brute force O(2**(m+n))
# def grid_traveller(m:int, n:int) -> int:
#     if m == 1 and n == 1:
#         return 1
#     if m == 0 or n == 0:
#         return 0
#     return grid_traveller(m-1,n) + grid_traveller(m,n-1)

# memoized O(m*n)
def grid_traveller(m:int, n:int,memo={}) -> int:
    pos = (m,n)
    if pos in memo:
        return memo[pos]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[pos] = grid_traveller(m-1,n,memo) + grid_traveller(m,n-1,memo)
    return memo[pos]


print(grid_traveller(1,1))
print(grid_traveller(2,3))
print(grid_traveller(3,2))
print(grid_traveller(3,3))
print(grid_traveller(18,18))