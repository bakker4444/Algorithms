## Is Unique

# Implement an algorithm to determine if a string has all unique characters.
# What is you cannot use additional data structure?

def isUniqueChars(str):
    if len(str) > 128:
        return False
    else:
        boolArray = [False] * 128
        for char1 in str:
            if boolArray[ord(char1)]:
                return False
            else:
                boolArray[ord(char1)] = True
        return True

print("abcd result: %s" % isUniqueChars("abcd"))
print("aba result: " +  str(isUniqueChars("aba")))

