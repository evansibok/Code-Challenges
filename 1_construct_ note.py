import math
import os
import random
import re
import sys


#
# Complete the 'constructNote' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note


def constructNote(magazine, note):
    # Write your code here
    # Using another list
    # If the element can be found in both `note` and `magazine`,
    # Compare the words in the hashtable with the note array,
    # If we get the exact same words, return True
    # If it isn't found, return False
    # Otherwise return True
    # Duplicate words -> Check index in the magazine
    # Words not found in both lists
    # Case sensitive words -> Do nothing, python is case sensitive by default during comparisons
    # If the output word doesn't match the note words, return False

    visited = set()
    word_check = []
    # Get each word in note
    for word in note:
        # If the word in note exists in magazine
        # and hasn't been previously checked
        if word in magazine and magazine.index(word) not in visited:
            # save the index to visited
            visited.add(magazine.index(word))
            # append the word to the word_check
            word_check.append(word)
        # if the index exists in visited
        else:
            # move on and check the next word
            continue

    # word_check list is expected to have
    # the exact same elements in notes
    # which means the length of both lists should be the same
    # If it isn't, we return False
    # otherwise, we return True
    if len(word_check) != len(note):
        return False
    else:
        return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    magazine_count = int(input().strip())

    magazine = []

    for _ in range(magazine_count):
        magazine_item = input()
        magazine.append(magazine_item)

    note_count = int(input().strip())

    note = []

    for _ in range(note_count):
        note_item = input()
        note.append(note_item)

    result = constructNote(magazine, note)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
