# Method 2: This method uses recursion to solve the above problem.
#
# Approach :
# The problem can be decomposed into a combination of smaller instances. Say, if the celebrity of N-1
# persons is known, can the solution to N? There are two possibilities, Celebrity(N-1) may know N, or
# N already knew Celebrity(N-1). In the former case, N will be a celebrity if N. In the latter case,
# check that Celebrity(N-1) doesn’t know N.
# The above-mentioned approach use Recursion to find the celebrity among n persons. It is necessary to
# find a celebrity among n-1 persons. So while calculating the celebrity of i persons the function calls
# itself to find the celebrity of i-1 persons and continues doing so until the base case is found.
# Algorithm :
# Create a recursive function that takes an integer n.
# Check the base case, if the value of n is 0 then return 0.
# Call the recursive function and get the ID of celebrity from the first n-1 elements.
# If the id is -1 then assign n as celebrity and return the value.
# If the celebrity of first n-1 elements knows n-1 and n-1 does not know the celebrity then return n-1,
# (0 based indexing)
# If the celebrity of first n-1 elements does not know n-1 and n-1 knows the celebrity then return id
# of celebrity of n-1 elements, (0 based indexing)
# Else return -1
# Create a wrapper function and check whether the id returned by the function is really the celebrity or
# not.

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


# // Returns -1 if celebrity is not present. If present, returns id (value from 0 to n-1).
def findCelebrity(nSize):
    if nSize == 1:
        return nSize - 1

    cId = findCelebrity(nSize - 1)
    if cId == -1:
        return nSize-1
    # if the celebrity knows the nth person
    elif doesKnows(cId, nSize - 1) and not doesKnows(nSize - 1, cId):
        return nSize - 1
    # if the nth person knows the celebrity then return the id
    elif doesKnows(nSize - 1, cId) and not doesKnows(cId, nSize - 1):
        return cId
    else:
        return -1


def Celebrity(matSize):
    celId = findCelebrity(matSize)
    #  check if the celebrity found is really the celebrity
    if celId == -1:
        return celId
    else:
        c1 = 0
        c2 = 0
        for i in range(matSize):
            if i != celId:
                c1 += doesKnows(celId, i)
                c2 += doesKnows(i, celId)

        # if the person is known to everyone.
        if c1 == 0 and c2 == matSize - 1:
            return celId
        return -1


if __name__ == '__main__':
    n = 4
    idOfCel = Celebrity(n)
    if idOfCel == -1:
        print("No celebrity")
    else:
        print(f"celebrity present and id = {idOfCel} as index")


# Complexity Analysis:
# Time Complexity: O(n).
# The recursive function is called n times, so the time complexity is O(n).
# Space Complexity: O(1).
# As no extra space is required.


# but this below one takes o(n) time and space both . uses stack==========

# Approach: There are some observations based on elimination technique (Refer Polya’s How to Solve It book).
# If A knows B, then A can’t be a celebrity. Discard A, and B may be celebrity.
# If A doesn’t know B, then B can’t be a celebrity. Discard B, and A may be celebrity.
# Repeat above two steps till there is only one person.
# Ensure the remained person is a celebrity. (What is the need of this step?)
# The stack can be used to verify celebrity. Insert all the elements in the stack. If the size of the
# stack is greater than 1 then pop top 2 elements of the stack (represent them as A and B). Check if A
# knows B, then A can’t be a celebrity. If A doesn’t know B, then B can’t be a celebrity. So one of the
# element gets discarded and push the other element back in the stack. In this way, only one element will
# be left. Check if the element left in the stack is celebrity or not. If yes print the id else print -1.
