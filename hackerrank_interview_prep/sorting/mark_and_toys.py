"""
Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. There are a 
number of different toys lying in front of him, tagged with 
their prices. Mark has only a certain amount to spend, and 
he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the 
maximum number of toys Mark can buy?
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices.sort()
    total_cost = 0
    toy_count = 0
    for toy in prices:
        if total_cost + toy > k:
            break

        total_cost += toy
        toy_count += 1
    return toy_count


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
