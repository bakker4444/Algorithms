## URLify

# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

## Test input
testInput = "Mr John Smith    ", 13

## espected output: "Mr%20John$20Smith"

def urlify(testInput):
    inputString, inputLength = testInput
    print(inputString, inputLength)
    result = ""
    for i in range(inputLength):
        if inputString[i] == " ":
            result += "%20"
        else:
            result += inputString[i]
    result += "]"
    return result

print(urlify(testInput))
