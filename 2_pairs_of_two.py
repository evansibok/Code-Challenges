# Find all the pairs of two integers in an unsorted array that
#  sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11]
#  and the sum is 7, your program should return [[11, -4], [2, 5]]
#  because 11 + -4 = 7 and 2 + 5 = 7.


# [3, 5, 2, -4, 8, 11] -> 7

# Should return [[11, -4], [2, 5]]

# UPER APPROACH

# SOLUTION IN QUADRATIC TIME COMPLEXITY

test_arr = [3, 5, 2, -4, 8, 11]
sum1 = 7

# key, value, index


def pairs_of_two(arr, sum):
    result = []

    # Move through the list getting each element
    for first in range(len(arr)):
        # Save the first element to a temp variable
        prev = arr[first]
    # Then get the element after it and add them together
        for second in range(first + 1, len(arr)):
            # If it sums up to the sum
            if prev + arr[second] == sum:
                # Add the two numbers to a list
                # save somewhere
                result.append([prev, arr[second]])
    # and return a list of the pairs at the end
    return result


print("pairs", pairs_of_two(test_arr, sum1))


# SOLUTION IN LINEAR TIME COMPLEXITY

test = [3, 5, 2, -4, 8, 11]
target = 7

# target-> 7
# hashtable key -> difference
# hashtable value -> element itself


def new_pairs_of_two(arr, target):
    # Initialize a hashtable to track the difference
    diff = {}
    result = []

    # Move through the list
    # Get the element in the list
    for element in arr:
        # Check if the element exists in the hashtable
        if element in diff:
            # If it does,
            # append a list of the element and
            # it's corresponding value on the hashtable to the result
            result.append([diff[element], element])
        # Otherwise
        else:
            # Subtract the element from the target and get the difference
            difference = target - element
            # Add the element as value to the hashtable
            # And the difference as the corresponding key
            diff[difference] = element
    # At the end, return the resulting array of all arrays
    return result


print("new pairs", new_pairs_of_two(test, target))
