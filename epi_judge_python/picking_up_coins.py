from test_framework import generic_test


def maximum_revenue(coins):
    # TODO - you fill in here.
    def max_revenue_helper(a, b):
        if a > b:
            return 0

        if max_revenue[a][b] == 0:
            max_revenue[a][b] = max(
                    coins[b] + min(max_revenue_helper(a+1, b-1),
                                   max_revenue_helper(a, b-2)),
                    coins[a] + min(max_revenue_helper(a+1, b-1),
                                   max_revenue_helper(a+2, b)))
        return max_revenue[a][b]

    max_revenue = [[0] * len(coins) for _ in range(len(coins))]
    return max_revenue_helper(0, len(coins)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
