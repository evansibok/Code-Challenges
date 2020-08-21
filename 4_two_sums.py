# Given an array of integers, return indices of the two
# numbers such that they add up to a specific target.
# You may assume that each input would have exactly
# one solution, and you may not use the same element twice.

# Example:

# nums = [2, 7, 11, 15]
# target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# SOLUTION IN LINEAR TIME COMPLEXITY
arr = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    # A target
    # Array
    # Return the indices of two numbers that sum up to the target

    # Create a hashtable to track the difference
    diff = {}
    # Move through the list getting each number and index
    for index, num in enumerate(nums):
        # If num is in hashtable
        if num in diff:
            # return a list of
            # [<index of difference>, index of current number]
            return [diff[num], index]
        else:
            # Subtract the number from the target
            difference = target - num
            # Save the difference as the key
            # and the number's index as the value on the hashtable
            diff[difference] = index


print("two sums", twoSum(arr, target))
