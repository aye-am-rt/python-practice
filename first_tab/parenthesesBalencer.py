# Python3 Program to find
# minimum number of '(' or ')'
# must be added to make Parentheses
# string valid.

# Function to return required
# minimum number


def minParentheses(p):
    # maintain balance of string
    bal = 0
    ans = 0
    for i in range(0, len(p)):
        if p[i] == '(':
            bal += 1
        else:
            bal += -1

        # It is guaranteed bal >= -1
        if bal == -1:
            ans += 1
            bal += 1
    return bal + ans


# Driver code
if __name__ == '__main__':
    p = "()))"

    # Function to print required answer
    print(minParentheses(p))
    a = float('inf')
    b = int(45613542121321313213246545)
    c = float('-inf')
    print(a > b)
    print(a < c)
# If you just need a number that's bigger than all others, you can use
#
# float('inf')
# in similar fashion, a number smaller than all others:
#
# float('-inf')
# This works in both python 2 and 3.

#
# In Python integers will automatically switch from a fixed-size int representation into a variable
# width long representation once you pass the value sys.maxint, which is either 231 - 1 or 263 - 1
# depending on your platform. Notice the L that gets appended here:
#
# >>> 9223372036854775807
# 9223372036854775807
# >>> 9223372036854775808
# 9223372036854775808L
# From the Python manual:
#
# Numbers are created by numeric literals or as the result of built-in functions and operators.
# Unadorned integer literals (including binary, hex, and octal numbers) yield plain integers unless
# the value they denote is too large to be represented as a plain integer, in which case they yield a
# long integer. Integer literals with an 'L' or 'l' suffix yield long integers ('L' is preferred
# because 1l looks too much like eleven!).
#
# Python tries very hard to pretend its integers are mathematical integers and are unbounded.
# It can, for instance, calculate a googol with ease:
#
# >>> 10**100
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000L
# shareimprove this answer
# edited Sep 30 '11 at 1:12
# answered Sep 30 '11 at 1:07
#
# John Kugelman
# 277k5959 gold badges438438 silver badges492492 bronze badges
# 36
# To add to the confusion, Python's long isn't like Java's long - it's rather closer to BigInteger.
# In python3, seems there is no L suffix, and it's just int, not long,
# no matter how large the number is. – Eric Wang Feb 19 at 13:18
# 33
#
# For Python 3, it is
#
# import sys
# max = sys.maxsize
# min = -sys.maxsize -1
# shareimprove this answer
# edited Dec 18 '17 at 2:18
# user6655984
# answered Mar 2 '17 at 0:09
#
# netskink
# 1,6751818 silver badges2626 bronze badges
# 2
# python 3 does not exist. see stackoverflow.com/questions/13795758/… – netskink Mar 28 '17 at 12:14
# 30
# well, python 3 does exist , thankfully(!); but sys.maxint doesn't exist in python 3
# (tl;dr: "sys.maxint constant was removed (in python3), since there is no longer a limit to
# the value of integers. However, sys.maxsize can be used as an integer larger than any practical
# list or string index." ) – michael Jul 16 '17 at 0:33
# 1
# Why create variables that shadow builtins such as min() and max()? – RoadRunner Jul 12 '18 at 0:38
# 1
# Look up 2’s compliment binary – netskink Jun 6 '19 at 14:11
# 1
# This answer is false. If it were true sys.maxsize ** 2 would not return a valid and correct
# value, yet it does. You should delete this answer. –
