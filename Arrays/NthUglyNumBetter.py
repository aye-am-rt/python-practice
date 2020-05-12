"""Ugly Numbers
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number.

Examples:
Input  : n = 7
Output : 8

Method 2 (Use Dynamic Programming)
Here is a time efficient solution with O(n) extra space. The ugly-number sequence is 1, 2, 3, 4, 5,
 6, 8, 9, 10, 12, 15, …
     because every number can only be divided by 2, 3, 5, one way to look at the sequence is to
     split the sequence to three groups as below:
     (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, …

     We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2,
     3, 5. Then we use similar merge method as merge sort, to get every ugly number from the three
      subsequence. Every step we choose the smallest one, and move one step after.

1 Declare an array for ugly numbers:  ugly[n]
2 Initialize first ugly no:  ugly[0] = 1
3 Initialize three array index variables i2, i3, i5 to point to
   1st element of the ugly array:
        i2 = i3 = i5 =0;
4 Initialize 3 choices for the next ugly no:
         next_multiple_of_2 = ugly[i2]*2;
         next_multiple_of_3 = ugly[i3]*3
         next_multiple_of_5 = ugly[i5]*5;
5 Now go in a loop to fill all ugly numbers till 150:
For (i = 1; i < 150; i++ )
{
    /* These small steps are not optimized for good
      readability. Will optimize them in C program */
    next_ugly_no  = Min(next_multiple_of_2,
                        next_multiple_of_3,
                        next_multiple_of_5);

    ugly[i] =  next_ugly_no

    if (next_ugly_no  == next_multiple_of_2)
    {
        i2 = i2 + 1;
        next_multiple_of_2 = ugly[i2]*2;
    }
    if (next_ugly_no  == next_multiple_of_3)
    {
        i3 = i3 + 1;
        next_multiple_of_3 = ugly[i3]*3;
     }
     if (next_ugly_no  == next_multiple_of_5)
     {
        i5 = i5 + 1;
        next_multiple_of_5 = ugly[i5]*5;
     }

}/* end of for loop */
6.return next_ugly_no
"""


# Time Complexity: O(n)
# Auxiliary Space: O(n)
def getNthUglyNo_DP(nth):
    uglyNums = [0] * nth  # To store ugly numbers
    uglyNums[0] = 1
    i2 = i3 = i5 = 0

    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n]
    for i in range(1, nth):
        uglyNums[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        if uglyNums[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = uglyNums[i2] * 2

        if uglyNums[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = uglyNums[i3] * 3

        if uglyNums[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = uglyNums[i5] * 5

    return uglyNums[-1]


def main():
    n = 150
    print(getNthUglyNo_DP(n))


if __name__ == '__main__':
    main()
# Time Complexity: O(n)
# Auxiliary Space: O(n)
