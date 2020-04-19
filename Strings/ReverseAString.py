# Function to reverse a string
def reverse(strToRev):
    strToRev = strToRev[::-1]
    return strToRev


# Driver program to test above functions
string = "abc"
string = reverse(string)
print("Reversed string is ==  " + string)
print("we are doing work on same string here so it maintains its state means once it is "
      "reversed \nif we again reverse it ..it wil become like original again ==")
print("another way to reverse = ")
revStr = ''.join(reverse(string))
print(revStr)
