"""

No Repeats Please

Return the number of total permutations of the provided string that don't have repeated consecutive letters.
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), but only 2 of
them (aba and aba) don't have the same letter (in this case a) repeating.

"""

def generatePermutation(current_permutation):
    if len(current_permutation) == 1:
        return [current_permutation]

    output = []
    *start, end = current_permutation
    for permutation in generatePermutation(start):
        for i in range(len(permutation) + 1):
            new = permutation[:i] + [end] + permutation[i:]
            output.append(new)

    return sorted(output)


def permAlone(str):

    perm_list = generatePermutation(str)
    result = len(perm_list)
    for permutation in perm_list:
        for idx, letter in enumerate(permutation):
            if idx > 0:
                last_letter = permutation[idx-1]
                if last_letter == letter:
                    result -= 1
                    break

    return result


print(permAlone("aab"))
print(permAlone("aaa"))
print(permAlone("aabb"))
print(permAlone("abcdefa"))
print(permAlone("abfdefa"))
print(permAlone("zzzzzzzz"))
print(permAlone("a"))
print(permAlone("aaab"))
print(permAlone("aaabb"))