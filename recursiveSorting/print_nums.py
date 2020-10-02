
# Can we define this problem in terms of identical subproblems?
# ​
# Goal: print the numbers from x to y-1.
# ​
# print numbers from x to y-1:
# ^^^^^^^^^^^^^^^^^^
#     if x >= y: return
#     print x
#     print numbers from x+1 to y-1
#     ^^^^^^^^^^^^^^^^^^
# ​
# Printing numbers from 1 to 5 is the same as:
#     Printing 1
#     Printing numbers from 2 to 5
# ​
# 1
# 2
# 3
# 4
# 5


def print_nums(x, y):
    if x >= y:
        return


​
print(x)
​
print_nums(x + 1, y)
​
​
