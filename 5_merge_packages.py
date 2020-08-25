# Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of an item, implement a function merge_packages that finds the first two items in the items array whose sum of weights equals the given weight limit limit.

# Your function should return a pair[i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

# Examples:

# Input: items = [4, 6, 10, 15, 16], limit = 21
# Output: [3, 1]
# Explanation: The weight of the items at indices 3 and 1 sum up to the specified limit.

# [execution time limit] 4 seconds(py3)

# [input] array.integer items

# A list of item weights.

# [input] integer limit

# The weight limit we're aiming for by merging two packages.

# [output] array.integer

# A pair of item indices indicating the two items that, when merged, reach the specified limit.

# SOLUTION
items = [4, 6, 10, 15, 16]
limit = 21


def merge_packages(items, limit):
    # Given package with weight limit
    # and an array of integers "items"
    # Each integer represents
    # Function finds two items in the array whose
    # sum of weights equals the given weight limit

    # Should return a pair [i, j]
    # of the indices of the item weights
    # ordered such that i > j
    # If the pair doesn't exist
    # return empty array
    if len(items) <= 1:
        return []

    # Initialize a hashtable to track the difference
    diff = {}  # O(n) -> Dependent on the number of input items
    # Move through each element in the list
    for index, item in enumerate(items):
        # Get the element and the index
        # For each element
        # If the limit is 1 then we can't have two items
        # that sum up to the limit
        # As an item has to weigh at least 1
        # In this case return an empty list
        if item not in diff and limit == 1:
            return []
        # if the element exists in the hashtable
        elif item in diff:
            # return the indices of both elements
            # with the greater index on the left
            if diff[item] > index:
                return [diff[item], index]
            elif index > diff[item]:
                return [index, diff[item]]
        # If element does not exist in the hashtable
        else:
            # Get the difference of the element from the target
            difference = limit - item
            # 0 = 1 - 1 => 0: 0
            # -1 = 1 - 2 => -1: 1
            # -2 = 1 - 3 => -2: 2
            # and save the difference as the key on the hashtable
            # and the index as the value
            diff[difference] = index

# Time Complexity -> O(n)
# Space Complexity -> O(n)


print('merge_packages', merge_packages(items, limit))
