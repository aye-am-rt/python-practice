# Implementation:
# Variables to be used:
#
# maxReach The variable maxReach stores at all time the maximal reachable index in the array.
# step The variable step stores the number of steps we can still take(and is initialized
# with value at index 0,i.e. initial number of steps)
# jump jump stores the amount of jumps necessary to reach that maximal reachable position.
# Given array arr = 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9
#
# maxReach = arr[0] // arr[0] = 1, so the maximum index we can reach at the moment is 1.
# step = arr[0] // arr[0] = 1, the amount of steps we can still take is also 1.
# jump = 1 // we will always need to take at least one jump.
# Now, starting iteration from index 1, the above values are updated as follows:
# First we test whether we have reached the end of the array, in that case we just need to
# return the jump variable.
# if (i == arr.length - 1)
#     return jump
# Next we update the maxReach. This is equal to the maximum of maxReach and
# i+arr[i](the number of steps we can take from the current position).
# maxReach = Math.max(maxReach,i+arr[i])
# We used up a step to get to the current index, so steps has to be decreased.
# step--
# If no more steps are remaining (i.e. steps=0, then we must have used a jump.
# Therefore increase jump. Since we know that it is possible somehow to reach maxReach,
# we again initialize the steps to the number of steps to reach maxReach from position i.
# But before re-initializing step, we also check whether a step is becoming zero or negative.
# In this case, It is not possible to reach further.
# if (step == 0) {
#     jump++
# if(i>=maxReach)
# return -1
# step = maxReach - i
# }


# python program to count Minimum number
# of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):
    # The number of jumps needed to reach the starting index is 0
    if n <= 1:
        return 0

    # Return -1 if not possible to jump
    if arr[0] == 0:
        return -1

    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0]
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the amount of jumps necessary to reach that maximal reachable position
    jump = 1

    # Start traversing array

    for i in range(1, n):
        # Check if we have reached the end of the array
        if i == n - 1:
            return jump

            # updating maxReach
        maxReach = max(maxReach, i + arr[i])

        # we use a step to get to the current index
        step -= 1

        # If no further steps left
        if step == 0:
            # we must have used a jump
            jump += 1

            # Check if the current index/position or lesser index
            # is the maximum reach point from the previous indexes
            if i >= maxReach:
                return -1

            # re-initialize the steps to the amount
            # of steps to reach maxReach from position i.
            step = maxReach - i
    return -1


# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)

# Calling the minJumps function
print("Minimum number of jumps to reach end is %d " % minJumps(arr, size))
