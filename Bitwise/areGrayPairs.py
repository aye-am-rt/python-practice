# two numbers are called gray pairs when they have exactly one bit different from each other.

if __name__ == '__main__':
    a = 12
    b = 8
    x = a ^ b
    print(f"a= {bin(a)}\nb= {bin(b)}\nx= {bin(x)}")
    print(f"normal x= {x}, bin(x)= {bin(x)}")
    print(f"normal x-1= {x-1},bin(x-1)= {bin(x-1)}")
    ans = True
    while x > 0:
        # if number is odd then it means its rightmost bit is 1.
        if x % 2 == 1 and x >> 1 > 0:
            ans = False
        x = x >> 1  # right shifting (arithmetic right shift)
        # the least-significant bit is lost and the most-significant bit is copied.
    print(ans)

    # other trick to find out just 1 bit is difference
    print(x & (x - 1) == 0)
