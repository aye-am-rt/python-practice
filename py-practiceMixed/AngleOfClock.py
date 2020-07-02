# cook your dish here


def get_angle(h, m, s):
    # a=(h*30-m*6-0.1*s)+(m*0.5+0.0083*s)
    a = 30 * h - 5.5 * m - 0.0917 * s
    return abs(min(360 - a, a))


if __name__ == '__main__':
    ql = [[3, 10, 0], [9, 59, 0], [10, 10, 450], [3, 30, 0], [9, 15, 0], [12, 0, 0]]
    al = []
    for q in ql:
        h = q[0]
        m = q[1]
        s = q[2]
        print("h=", h, " m=", m, " s=", s)
        if 1 <= h <= 12 and 0 <= m <= 60 and 0 <= s <= 60:
            a = get_angle(h, m, s)
            al.append(round(a, 3))
        else:
            print("wrong time given ")
            al.append(-1)
    print("the angle between hour and minute needle will be respectively ")
    # print(al,"degrees each",end="\n" )
    print("   ".join(map(str, al)) + "  degrees each")
