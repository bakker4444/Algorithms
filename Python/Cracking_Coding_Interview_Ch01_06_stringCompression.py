## String Compression

# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters(a-z).

def stringCompression(str1):
    if len(str1) < 2:
        return str1
    compressedString = compressed(str1)
    if len(str1) > len(compressedString):
        return compressedString
    else:
        return str1


def compressed(str1):
    result = ""
    currentChar = str1[0]
    countIndex = 0
    for i in range(len(str1)):
        if currentChar != str1[i]:
            result = result + currentChar + str(countIndex)
            currentChar = str1[i]
            countIndex = 1
        else:
            countIndex += 1
    result = result + currentChar + str(countIndex)
    print(str1)
    print(result)
    print(len(str1))
    print(len(result))
    return result

inputString = "aabcccccaaa"
print(stringCompression(inputString))
inputString = "aaa"
print(stringCompression(inputString))