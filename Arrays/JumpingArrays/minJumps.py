import sys


# import math
#
# print("GCD of 75 and 30 is ", math.gcd(75, 30))
# a, b, c, d = "abcde", "xy", 2, 15.06
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))
#
# # Reversing Strings
# list1 = ["a", "b", "c", "d"]
# print(list1[::-1])
#
# # Reversing Numbers
# list2 = [1, 3, 6, 4, 2]
# print(list2[::-1])
#
# # Transpose a Matrix
# # Transposing a matrix involves converting columns into rows. In python we can achieve
# # it by designing some loop structure to iterate through the elements in the matrix
# # and change their places or we can use the following script involving zip function in conjunction
# # with the * operator to unzip a list which becomes a transpose of the given matrix.
#
# x = [[31, 17], [40, 51], [13, 12]]
# print(*zip(*x))
#
# # print("Mean of the above list of numbers is: " + str(round(mean,2)))
#
# from collections import Counter
#
# word_set = " This is a series of strings to count " \
#            "many words . They sometime hurt and words sometime inspire " \
#            "Also sometime fewer words convey more meaning than a bag of words " \
#            "Be careful what you speak or what you write or even what you think of. " \
#     # Create list of all the words in the string
# word_list = word_set.split()
#
# # Get the count of each word.
# word_count = Counter(word_list)
#
# # Use most_common() method from Counter subclass
# print(word_count.most_common(3))
#
#
# def transpose(m):
#     rez = [[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]]
#     for row in rez:
#         return row
#
#
# print("result=", transpose([[1, 3, 5], [2, 4, 6]]))
# print("result=", transpose([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
# print("result=", transpose([[1, 4, 9]]))


# find out min jumps to reach array end.
# you can only jump to the length which is the number present at that index.
# solve it using dp.
# arr=[2,1,3,2,3,4,5,1,2,8]
# for dp 2 things required-
# 1. optimization or minimization problem.
# 2. overlapping sub-problems should be present.


def findMinJumps(arr):
    n = len(arr)

    # make min_jumps_array of same length as arr , its each index will
    # store the min num of jumps req to
    # reach that index in array.
    min_jumps_array = [0] + [100000] * (n - 1)

    # make jump_path_array which holds the location from where we jumped
    # to that index in original array.
    # means the last stop of jump, we can trace back our path.
    jump_path_array = [0] * n

    for i in range(1, n):
        for j in range(i):
            if i <= j + arr[j]:
                min_jumps_array[i] = min(min_jumps_array[i], min_jumps_array[j] + 1)
                jump_path_array[i] = j
                break

    print("given array ===  ", end=" ")
    print(arr)
    print("min_jumps_array =", min_jumps_array)
    print("jump path array =", jump_path_array)
    print("printing the path value of indices not the elements in array")
    #   str = 'Python' #initial string
    #   reversed=''.join(reversed(str))
    #   .join() method merges all of the characters resulting from the reversed
    #   iteration into a new string
    #   print(reversed) #print the reversed string

    c = n - 1
    p = ""
    while c:
        p = p + "--" + str(jump_path_array[c])
        c = jump_path_array[c]
    print(p[:1:-1])
    # stringName[::-1] # method2 of reversing  a string

    return min_jumps_array[n - 1]


if __name__ == "__main__":
    # l1 = [int(x) for x in input("give space separated positive numbers for list 1 = ").split()]
    # print("given array = ", l1)
    l1 = [2, 1, 3, 2, 3, 4, 5, 1, 2, 8]
    print("min jumps to reach end index = ", findMinJumps(l1))
