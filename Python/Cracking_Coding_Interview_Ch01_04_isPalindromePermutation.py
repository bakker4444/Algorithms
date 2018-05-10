## Palindrome Permutation

# Givin a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
#
# EXAMPLE
# Input : Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

def isPalindromePermutation(str1):
    oddCounterIndex = 0
    result = {}

    for i in str1:
        i = i.lower()
        if i != " ":
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1

    for i in result.keys():
        if result[i] % 2 == 0:
            continue
        else:                   # result[i] % 2 == 1 which means odd number
            oddCounterIndex += 1
            if oddCounterIndex > 1:
                return False
    return True

print(isPalindromePermutation("Tact Coa"))
print(isPalindromePermutation("abc def dcb a"))
