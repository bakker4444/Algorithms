## Check Permutation

# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(str1, str2):
    strArray = [0] * 128

    for char1 in str1:
        strArray[ord(char1)] += 1

    for char2 in str2:
        strArray[ord(char2)] -= 1
        if strArray[ord(char2)] < 0:
            print(strArray)
            return False
    return True

print(checkPermutation("abcdef", "febcda"))