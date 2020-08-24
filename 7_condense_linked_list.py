# Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N

# Explanation: The input list contains redundant nodes(3), (6), and (2), so those should be removed from the list.

# [execution time limit] 4 seconds(py3)

# [input] linkedlist.integer node

# The head node of the linked list.

# [output] linkedlist.integer

# The head node of the updated linked list.

# SOLUTION
# Singly-linked lists are already defined with this interface:


# class ListNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.next = None

#     def __repr__(self):
#         return f"value: {self.value}, next: {self.next}"


def condense_linked_list(node):
    # Initialize a visited list to track
    # previously occured values
    visited = []
    # Get the value of the current node
    cur_node = node
    # Move through the linked list
    while cur_node is not None:
        # If the current node's value exists in visited
        if cur_node.value in visited:
            # Move to the next node
            cur_node = cur_node.next
        # Otherwise
        else:
            # Add it to visited
            visited.append(cur_node.value)
    # Return the new list which contains
    # unrepeated node values
    return visited
