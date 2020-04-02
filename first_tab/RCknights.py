# that a knight can attack only on a different color.
# We can take help of this fact and use it for our purpose. Now as we know knight attacks on different
# color so we can keep all knights on the same color i.e. all on white or all
# on black. Thus making the highest number of knights which can be placed.
# To find the number of black or white, it is simply half of the total blocks on board.
# Total Blocks = n * m
# Blocks of the same color = (n * m) / 2


def HowManyKnights(r, c):
    if r <= 0 or c <= 0:
        return -1
    elif r == 1 or c == 1:
        return max(r, c)
    elif r == 2 or c == 2:
        if r == c or r == 3 or c == 3:
            return 4
        else:
            m = max(r, c)
            return 4 + (m % 4) * 2
    else:
        return ((r * c) + 1) // 2


if __name__ == "__main__":
    rows, columns = 10, 50
    print(HowManyKnights(rows, columns))
