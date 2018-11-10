from test_framework import generic_test


def calculate_largest_rectangle(heights):
    # TODO - you fill in here.
    s = []
    maxrect = 0
    for i, height in enumerate(heights + [0]):
        while s and heights[s[-1]] >= height:
            pillar_index = s.pop()
            pillar = heights[pillar_index]
            width = i - s[-1] - 1 if s else i
            maxrect = max(maxrect, pillar*width)
        s.append(i)

    return maxrect


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
