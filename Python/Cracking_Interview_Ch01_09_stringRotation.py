## String Rotation
#
# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is rotation of "erbottlewat").

# MORE PYTHONIC WAY
def stringRotation(str1, str2):
    return isSubstring(str1+str1, str2) if len(str1) == len(str2) else False

def isSubstring(str1, str2):
    (longStr, shortStr) = (str1, str2) if len(str1) >= len(str2) else (str2, str1)
    return True if longStr.find(shortStr) >= 0 else False


# TEST
string1 = "erbottlewat"
string2 = "waterbottle"
print(stringRotation(string1, string2))     ## expect True

string3 = "erbottlewata"
string4 = "waterbottleb"
print(stringRotation(string3, string4))     ## expect False
