"""Stock Buy Sell to Maximize Profit
The cost of a stock on each day is given in an array, find the max profit that you can make by
 buying and selling in those days. For example, if the given array is
 {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling
 on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in
 decreasing order, then profit cannot be earned at all.

 Efficient approach: If we are allowed to buy and sell only once, then we can use following
  algorithm. Maximum difference between two elements. Here we are allowed to buy and sell
  multiple times.
Following is algorithm for this problem.

Find the local minima and store it as starting index. If not exists, return.
Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
Update the solution (Increment count of buy sell pairs)
Repeat the above steps if end is not reached.

 """


def stockBuySell(priceArray, ln):
    if n < 2:
        return
    i = 0
    while i < ln - 1:
        while i < ln - 1 and priceArray[i + 1] < priceArray[i]:
            i += 1
        if i == n - 1:
            break
        buy = i
        i += 1
        while i < ln - 1 and priceArray[i + 1] > priceArray[i]:
            i += 1
        sell = i
        print(f"buy on {buy} index price and sell on {sell} index price for max profit")


if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695]
    # price = [1, 2, 3, 4, 5, 6]
    n = len(price)
    stockBuySell(price, n)
