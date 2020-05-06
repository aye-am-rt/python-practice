# Find the number of jumps to reach X in the number line from zero
# Given an integers X. The task is to find the number of jumps to reach a point X in the
# number line starting from zero.
#
# Note: The first jump made can be of length one unit and each successive jump will be
# exactly one unit longer than the previous jump in length. It is allowed to go either left
# or right in each jump.
#
# Examples:
# Input : X = 8
# Output : 4
# Explanation :
# 0 -> -1 -> 1 -> 4-> 8 are possible stages.
#
# Input : X = 9
# Output : 5
# Explanation :
# 0 -> -1 -> -3 -> 0 -> 4-> 9 are
# possible stages

"""Approach : On observing carefully, it can be said easily that:

If you have always jumped in the right direction then after n jumps you will be at the point
 p = 1 + 2 + 3 + 4 + … + n.
If instead of jumping right, you jumped left in the kth jump, you would be at point p – 2k.
Moreover, by carefully choosing which jumps to go left and which to go right, after n jumps,
you can be at any point between n * (n + 1) / 2 and – (n * (n + 1) / 2) with the same parity
as n * (n + 1) / 2.
Keeping the above points in mind, what you must do is simulate the jumping process, always
jumping to the right, and if at some point, you’ve reached a point that has the same parity
as X and is at or beyond X, you’ll have your answer."""


def countJumpsToReachN(num):
    num = abs(num)
    ansJump = 0
    # Continue till number is lesser or not in same parity
    while int(ansJump * (ansJump + 1) / 2) < num or \
            (int(ansJump * (ansJump + 1) / 2) - 1) & 1:
        ansJump += 1
    return ansJump


if __name__ == '__main__':
    n = 9
    print(countJumpsToReachN(n))
