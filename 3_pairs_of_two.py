# Find all the pairs of two integers in an unsorted array that
#  sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11]
#  and the sum is 7, your program should return [[11, -4], [2, 5]]
#  because 11 + -4 = 7 and 2 + 5 = 7.


# [3, 5, 2, -4, 8, 11] -> 7

# Should return [[11, -4], [2, 5]]

# UPER

# Move through the list getting each element
# Save the first element to a temp variable
# Then get the element after it and add them together
# If it sums up to the sum, I'll add the two numbers to a list
# save somewhere
# and return a list of the pairs at the end

sum1 = 7

test_arr = [3, 5, 2, -4, 8, 11]

# key, value, index


def pairs_of_two(arr, sum):
    result = []

    for first in arr:
        prev = first
        for second in range(1, len(arr)):
            if prev + arr[second] == sum:
                result.append([prev, arr[second]])
    return result


print(pairs_of_two(test_arr, sum1))
