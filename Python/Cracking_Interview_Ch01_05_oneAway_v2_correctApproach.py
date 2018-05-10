def oneAway(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 == len2:
        return checkReplaceStr(str1, str2)
    elif len1 - len2 == 1:
        return checkInsertDelete(str1, str2)
    elif len2 - len1 == 1:
        return checkInsertDelete(str2, str1)
    else:
        return False


def checkReplaceStr(str1, str2):
    diffCheck = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if diffCheck:
                return False
            diffCheck = True
    return True


def checkInsertDelete(str1, str2):
    diffCheck = False
    j = 0
    for i in range(len(str2)):
        if str1[i+j] != str2[i]:
            if diffCheck:
                return False
            diffCheck = True
            j += 1
    return True


print(oneAway("pale", "ple"))       ## expect True
print(oneAway("pales", "pale"))     ## expect True
print(oneAway("pale", "bale"))      ## expect True
print(oneAway("pale", "bake"))      ## expect False
