# NOT SOLVED

# -------------------------------------------------------------------
# You have an N by N grid of cells. The bottom-left corner is labeled (1, 1) and the top-right corner is labeled (N, N).

# Currently, there are lamps on this grid. The positions of these lamps are recorded in the list *lamps*. Each lamp is located at a distinct cell. Each lamp illuminates all squares that are in the same row, column, or diagonals as the lamp. The lamp is small enough that it will not block illumination from other lamps, All lamps are on by default.

# For instance, if N = 8, a lamp at cell (3, 5) would illuminate all yellow cells in the image below (see 'instance-1.png').

# You are part of a task force that is attempting to investigate how well-lit the grid cells are. If the task force visits a cell, it turns off all lamps that are in that cell, or in any adjacent cell to avoid damaging those lamps. Two cells are adjacent if they share an edge or a corner. After the task force turns off all the affected lamps, the task force checks to see if the current grid cell is still illuminated by some lamp, and notes whether the square was illuminated or in darkness. The task force turns on all lamps after completing its investigation.

# For example, if the task force visits cell (4, 4) labeled with a ? mark (see instance-2.png), they would turn off all lamps in the green squares. However, the task force cannot turn off any of the other lamps. Therefore, cell (4, 4) would be illuminated because the lamp at cell (6, 2) is still on.
# -------------------------------------------------------------------

# Q: Write a function checkIllumination(N, lamps, queries) that follows the function signature below:

# INPUTS
# N -> Integer representing the size of the grid
# lamps -> A list of L entries. Each entry is a list with 2 entries
# representing the x, y coordinates of a lamp
# queries -> A list of M entries. Each entry is a list with 2 entries
# representing the x, y coordinates of a query cell

# OUTPUT
# A list of M entries. Each entry should be either the string "LIGHT"
# if the corresponding query cell s illuminated or "DARK" otherwise

# EXAMPLES
# 1
# Input: N = 8, lamps = [[4, 3], [4, 4]], queries = [[3, 4], [7, 6]]
# Output: ["DARK", "LIGHT"]

# Explanation
# The image below corresponds to sample input 1. Lamps are at cells (4, 3) and (4, 4). Query cell (3, 4) is not illuminated because both lamps are adjacent and therefore turned off; thus the corresponding output is "DARK". Query cell (7, 6) is illuminated by the lamp (4, 3), which is not turned off because it is not adjacent to the query cell; thus the corresponding output is "LIGHT".

# 2
# Input: N = 8, lamps = [[1, 6], [5, 6], [7, 3], [3, 2]]
# queries = [[4, 3], [6, 6], [8, 1], [3, 2], [2, 3]]
# Output: ["DARK", "LIGHT", "DARK", "DARK", "LIGHT"]

# Explanation
# The image below corresponds to sample input 2. Query cells that are illuminated are colored yellow, and cells that are not illuminated are colored gray.


# Complete the checkIllumination function below.
def checkIllumination(N, lamps, queries):
    pass
