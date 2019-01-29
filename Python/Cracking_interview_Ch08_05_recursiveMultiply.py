## 08.05 Recursive Multiply
# Write a recursive function to multiply two positive integers without using the * operator.
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
##


## iterative approach
# time complexity : O(M), M==binary bit length from LSB to MSB
# space complexity : O(1)
def recursiveMultiply1(num1, num2):
    result = 0
    while num2 > 0:
        if num2 % 2 == 1:
            result += num1
        num1 = num1 << 1
        num2 = num2 >> 1
    return result


## recursive approach
# time complexity : O(M), M==binary bit length from LSB to MSB
# space complexity : O(M), call stack consumes memory
def recursiveMultiply2(num1, num2):
    result = 0
    if num1 == 0 or num2 == 0:
        return result

    if num2 % 2 == 1:
        return helper(num1<<1, num2>>1, result+num1)
    return helper(num1<<1, num2>>1, result)

def helper(num1, num2, result):
    if num2 == 0:
        return result
    if num2 % 2 == 1:
        return helper(num1<<1, num2>>1, result+num1)
    return helper(num1<<1, num2>>1, result)


if __name__ == "__main__":
    print(recursiveMultiply1(13, 28))
    print(recursiveMultiply1(0, 28))
    print(recursiveMultiply1(13, 0))
    print(recursiveMultiply1(4, 7))

    print(recursiveMultiply2(13, 28))
    print(recursiveMultiply2(0, 28))
    print(recursiveMultiply2(13, 0))
    print(recursiveMultiply2(4, 7))