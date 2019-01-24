## 08.01 Triple Step
#
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.


## dynamic programming
## time complexity : O(N)
## space complexity : O(1)
def hop(n):
    if n < 3:
        return [1,1,2][n]

    contents = []
    a, b, c = 1, 1, 2
    for i in range(3, n):
        result = a + b + c
        a, b, c = b, c, result
    return a+b+c


if __name__ == "__main__":
    for i in range(1, 11):
        print("{} stair(s) : {}".format(i, hop(i)))
