# NOT SOLVED

# Complete the 'isCurrency' function below.

# The function is expected to return a BOOLEAN.
# The function accepts STRING strAmount as parameter.


# Does string represent valid currency amount
# return True, if yes

# PROPERTIES OF SUCH STRINGS
# - amount consists of base 10 digits
# - amount may optionally contain thousands separators using the ',' character
# - if ',' is present, it must be present at each thousands increment
# after/before every three digits
# - amount must be prefixed by currency symbol (Dollars, Euros and Japanese Yen only)
# - negative amount must be "-$23" or "($23)"
# - dollar and euro amount may contain cents, represented to exactly two decimals
# - if decimal point is present, cents must be specified
# - Yen amounts don't have decimal points
# - amount may not contain leading zero unless it is zero dollars and zero euros
# and cents must be specified
# - other characters, including leading or trailing whitespace, is invalid

# Valid:
# "$450", "-€23", "(¥2500)", "$2,200.00", "€0.23"

# Invalid:
# "cat", "£23", "(¥2500", "$25,0", "-($3.50)",
# "$25.00", "$-50", " $2.25", "$65.", "$82.", "20.50", "¥1200,000"

# currency = {
#     "dollar": "$",
#     "euro": "€",
#     "yen": "¥"
# }

# character = ","
# if digits are greater than 3,
# add "," to front of every three digits starting from the end (there
# must be at least one digit before the ",")

# 1 - 1
# 10 - 2
# 100 - 3
# 1,000 - 4
# 10,000 - 5
# 100,000 - 6
# 1,100,000 - 7


def isCurrency(strAmount):
    # Write your code here
    currency = {
        "$": "$",
        "€": "€",
        "¥": "¥"
    }
    comma = ","
    dot = "."

    # Check trailing whitespace
    if " " in strAmount:
        return False

    # check hexadecimal
    if "0x" in strAmount:
        return False

    # check that currency is in string
    # and currency is not first char
    # and string is not prefixed by "-" or "()"
    for cur in currency:
        if cur in strAmount and strAmount[0] is not "-" or strAmount[0] is not "(" and strAmount[0] is not cur:
            return False

    for cur in currency:
        if cur in strAmount and strAmount[1] == 0 and dot in strAmount and len(strAmount) < 5:
            return False
