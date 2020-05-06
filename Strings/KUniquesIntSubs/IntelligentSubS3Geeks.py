if __name__ == '__main__':
    str1 = "hellolleo"
    a = str1.partition("ll")
    print("a = ", a)  # ('he', 'll', 'olleo')  returns tuple
    b = str1.rpartition("ll")
    print("b = ", b)  # b =  ('hello', 'll', 'eo') returns tuple

    print(str1.split("ll"))  # ['he', 'o', 'eo']
    print(str1.split("l"))  # ['he', '', 'o', '', 'eo']
