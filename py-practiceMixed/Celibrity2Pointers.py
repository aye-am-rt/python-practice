# Method 4: This method uses Two Pointers technique to solve the above problem.
#
# Approach: The idea is to use two pointers, one from start and one from the end. Assume the start person
# is A, and the end person is B. If A knows B, then A must not be the celebrity. Else, B must not be the
# celebrity. At the end of the loop, only one index will be left as a celebrity. Go through each person
# again and check whether this is the celebrity.
# The Two Pointer approach can be used where two pointers can be assigned, one at the start and other at
# the end and the elements can be compared and the search space can be reduced.
# Algorithm :
# Create two indices a and b, where a = 0 and b = n-1
# Run a loop until a is less than b.
# Check if a knows b, then a can be celebrity. so incement a, i.e. a++
# Else b cannot be celebrity, so decrement b, i.e. b–
# Assign a as the celebrity
# Run a loop from 0 to n-1 and find the count of persons who knows the celebrity and the number of people
# whom the celebrity knows. if the count of persons who knows the celebrity is n-1 and the count of people
# whom the celebrity knows is 0 then return the id of celebrity else return -1.

# more like static variable in java global.
MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]


def doesKnows(a, b):
    if 0 <= a < 4 and 0 <= b < 4:  # check for index less than matrix size
        return True if MATRIX[a][b] == 1 else False
    else:
        return False


def FindTheCelebrity(nSize):
    left = 0
    right = nSize - 1
    while left < right:
        if doesKnows(left, right):
            left += 1
        else:
            right -= 1

    for i in range(nSize):
        # // If any person doesn't  know 'left' or 'left' doesn't  know any person, return -1
        if i != left and (doesKnows(left, i) or not doesKnows(i, left)):
            return -1

    return left


if __name__ == '__main__':
    n = 4
    idOfCel = FindTheCelebrity(n)
    if idOfCel == -1:
        print("No celebrity")
    else:
        print(f"celebrity present and id = {idOfCel} as index")


# Complexity Analysis:
# Time Complexity: O(n).
# Total number of comparisons 2(N-1), so the time complexity is O(n).
# Space Complexity : O(1).
# No extra space is required.
