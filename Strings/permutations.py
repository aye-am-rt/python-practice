from collections import OrderedDict

statesAndCapitals = OrderedDict([('Gujarat', 'Gandhinagar'), ('Maharashtra', 'Mumbai'),
                                 ('Rajasthan', 'Jaipur'), ('Bihar', 'Patna')])
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)

# Iterating over values
for capital in statesAndCapitals.values():
    print(capital)

# Iterating over keys
for state in statesAndCapitals:
    print(state)


def printRecursivePermutations(a, left, right):
    if left == right:
        print(''.join(a), end=" ")
    else:
        for i in range(left, right):
            a[left], a[i] = a[i], a[left]
            printRecursivePermutations(a, left + 1, right)
            a[left], a[i] = a[i], a[left]


if __name__ == "__main__":
    string = "abc"
    printRecursivePermutations(list(string), 0, len(string))
