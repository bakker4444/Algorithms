## One Away

# There are types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    letterCountArray = [ 0 ] * 128

    for char1 in str1:
        letterCountArray[ord(char1)] += 1

    for char2 in str2:
        letterCountArray[ord(char2)] -= 1
        if letterCountArray[ord(char2)] < -1:
            return False

    countIndex = 0
    for element1 in letterCountArray:
        if element1 >= 1 or element1 <= -1:
            countIndex += 1
            if countIndex > 1:
                return False
    return True

# print(oneAway("pale", "ple"))       ## expect True
# print(oneAway("pales", "pale"))     ## expect True
print(oneAway("pale", "bale"))      ## expect True
# print(oneAway("pale", "bake"))      ## expect False
