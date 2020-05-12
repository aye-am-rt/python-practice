def sortByModulo(numArray, K):
    dcMods = {}
    for i, elem in enumerate(numArray):
        dcMods[elem] = numArray[i] % K
        # dcMods[elem] = elem % K
    print(dcMods)
    dcMods = sorted(dcMods.items(), key=lambda x: (x[1], x[0]))
    return dcMods


if __name__ == '__main__':
    arr = [10, 3, 2, 6, 12]
    k = 4
    print(sortByModulo(arr, k))
    print("**********this is just for some testing not related to program*************")
    # when you just sort a dictionary python prints its keys in sorted order no effect on dictionary
    checkDic = {12: "qw", 2: "rt", 1: "fgh", 41: "41"}
    print(sorted(checkDic))
    print(checkDic)

"""
**************************************************
enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is
to be started, by default it is 0

***************************************************
# Python program to illustrate enumerate function in loops

l1 = ["eat","sleep","repeat"]
# printing the tuples in object directly
for ele in enumerate(l1):
    print ele
    
Output:
(0, 'eat')
(1, 'sleep')
(2, 'repeat')

**************************

# changing index and printing separately
for count,ele in enumerate(l1,100):
    print count,ele

# output ******
100 eat
101 sleep
102 repeat




# Python program to illustrate
# enumerate function
l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print "Return type:",type(obj1)
print list(enumerate(l1))

# changing start index to 2 from 0
print list(enumerate(s1,2))
Output:

Return type: < type 'enumerate' >
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

 """
