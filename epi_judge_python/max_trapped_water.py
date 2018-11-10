from test_framework import generic_test


def get_max_trapped_water(heights):
    # TODO - you fill in here.
    maxwater = 0

    left, right = 0, len(heights)-1
    while left < right:
        maxwater = max(min(heights[left], heights[right])*(right-left), maxwater)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return maxwater


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
