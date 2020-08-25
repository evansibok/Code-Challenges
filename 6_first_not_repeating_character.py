# Given a string s consisting of small English letters, find and return the first instance of a non - repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# first_not_repeating_character(s) = 'c'.

# There are 2 non - repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# first_not_repeating_character(s) = '_'.

# There are no characters in this string that do not repeat.

# [execution time limit] 4 seconds(py3)

# [input] string s

# A string that contains only lowercase English letters.

# [output] char

# The first non - repeating character in s of '_' if there are no characters that do not repeat.

# SOLUTION
s = "abacabaabacaba"


def first_not_repeating_character(s):
    # String
    # Contains small english letters
    # Find characters that are not repeated in the String
    # Return the first letter found
    # if there is no character is not repeated
    # return "_" instead

    new_string = s.lower()
    seen = []
    occured_once = []  # O(n) + O(n) + O(n) -> 3n -> O(n)

    # Move through the lowercase String
    # Get each character
    for letter in new_string:
        # If character not in seen
        if letter not in seen:
            # Add it to the seen list
            seen.append(letter)  # O(n^2)

    # Run a count to check how many times letters
    # from the seen list occurs in the String
    for char in seen:
        # If the character occurs only once
        if new_string.count(char) == 1:
            # Add it to the new occured_once list
            occured_once.append(char)  # O(n^2)

    # If the occured_once list is empty
    # It means there are no characters that occurs only once
    if not occured_once:
        # return "_"
        return "_"
    # Otherwise return the first letter that occurs once
    else:
        return occured_once[0]

# Time Complexity -> O(n^2)
# Space Complexity -> O(n)


print('first_not_repeated', first_not_repeating_character(s))
