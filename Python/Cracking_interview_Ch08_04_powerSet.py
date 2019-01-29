## 08.04 Power Set
# Write a method to return all subsets of a set.
##


from copy import deepcopy

def powerSet(S):
    if not S or len(S) == 0:
        return [[]]

    result = []
    helper(result, S, len(S)-1)

    return result


def helper(result, S, idx):
    if idx == -1:
        result.append([])
    else:
        helper(result, S, idx-1)
        subsets = deepcopy(result)
        for arr in subsets:
            arr.append(S[idx])
        result.extend(subsets)



if __name__ == "__main__":
    print(powerSet([1]))
    print(powerSet([1, 2]))
    print(powerSet([1, 2, 3]))
    print(powerSet([1, 2, 3, 4]))
