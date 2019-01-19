## 412. Fizz Buzz
#
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#     n = 15,
#     Return:
#         [
#             "1",
#             "2",
#             "Fizz",
#             "4",
#             "Buzz",
#             "Fizz",
#             "7",
#             "8",
#             "Fizz",
#             "Buzz",
#             "11",
#             "Fizz",
#             "13",
#             "14",
#             "FizzBuzz"
#         ]
##


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            temp = ""
            if i % 3 != 0 and i % 5 != 0:
                temp = str(i)
            else:
                if i % 3 == 0:
                    temp += "Fizz"
                if i % 5 == 0:
                    temp += "Buzz"
            result.append(temp)
        return result


if __name__ == "__main__":
    print(Solution().fizzBuzz(0))
    print(Solution().fizzBuzz(1))
    print(Solution().fizzBuzz(2))
    print(Solution().fizzBuzz(3))
    print(Solution().fizzBuzz(30))