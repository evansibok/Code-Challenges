# array 1
# array 2

# return True if any of two numbers in array 1
# sum up any of the numbers in array 2

# E.g inputs = [-1, 8, 3] and tests = [3, 7, 2]
#     returns True because -1 + 3 is 2 and 2 appears
#     in tests array and -1 and 3 appears in inputs array

# both array are present
# each contain at least one element -> One element return False
# arrays are limited between 1 and 200 elements each

# get elements from array 2
# save in a visited set
# move through elements in array 1, starting from the first element
# add the element in the next index and check if the result is in visited
# if it is return True
# otherwise return False
# while the arrays length is greater than 1 and less than or equal to 200


def arraySum(inputs, tests):
    # Write your code here
    if len(inputs) < 1:
        return False

    if (len(inputs) > 1 and len(inputs) <= 200) and (len(tests) > 1 and len(tests) <= 200):
        visited = set()
        # Move through the tests array
        for ele in tests:
            # if element has not been seen
            if ele not in visited:
                # Add it to visited to prevent duplicate values
                visited.add(ele)
            else:
                # otherwise continue iterating through the array
                continue

        # Get the index of the inputs array
        for firstIndex in range(len(inputs)):
            # assign the element at that index to a prev value
            # to enable addition and prevent duplicate addition
            prev = inputs[firstIndex]
            # move through the inputs array
            # starting from the element to the right of the prev
            # and stopping at the end of the array to prevent
            # starting from the beginning of the array
            for secondIndex in range(firstIndex + 1, len(inputs)):
                # perform the addition
                print("prev, next", prev, inputs[secondIndex])
                sum = prev + inputs[secondIndex]
                # check if the sum exists in visited
                if sum in visited:
                    # if it does, return True
                    return True
                # otherwise return False
                else:
                    return False
