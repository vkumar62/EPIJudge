from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    # TODO - you fill in here.
    sunset_bldgs = []

    for i, bldg in enumerate(sequence):
        while sunset_bldgs and bldg >= sequence[sunset_bldgs[-1]]:
            sunset_bldgs.pop()
        sunset_bldgs.append(i)
    return list(reversed(sunset_bldgs))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
