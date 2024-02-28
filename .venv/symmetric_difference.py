"""

Find the Symmetric Difference

The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the
two sets but not in both. For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.

Symmetric difference is a binary operation, which means it operates on only two elements. So to evaluate an expression
involving symmetric differences among three elements (A △ B △ C), you must complete one operation at a time.
Thus, for sets A and B above, and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

Create a function that takes two or more arrays and returns an array of their symmetric difference. The returned
array must contain only unique values (no duplicates).

"""

def sym(*args):
    answer = args[0]
    for idx, arr in enumerate(args):
        if idx > 0:

            left_join = [num for num in answer if num not in arr]
            right_join = [num for num in arr if num not in answer]

            new_arr = set(left_join + right_join)
            answer = new_arr
    return answer


print(sym([1, 2, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3], [5, 2, 1, 4, 5]))
print(sym([1, 2, 5], [2, 3, 5], [3, 4, 5]))
print(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]))
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))