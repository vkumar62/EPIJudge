from test_framework import generic_test


def minimum_messiness(words, line_length):
    # TODO - you fill in here.
    messiness = [float('inf')] * len(words)
    # consider word0 in the entire line
    remaining_spaces = line_length - len(words[0])
    messiness[0] = remaining_spaces**2

    for i in range(1, len(words)):
        remaining_spaces = line_length - len(words[i])
        messiness[i] = messiness[i-1] + remaining_spaces**2

        # Try to pull more words from previous line to this line
        for j in reversed(range(i)):
            remaining_spaces -= len(words[j]) + 1
            if remaining_spaces < 0:
                # This line is full. so break
                break

            if j-1 < 0:
                first_j = 0
            else:
                # Previous line has j-1 words. So use their messiness
                first_j = messiness[j-1]

            messiness[i] = min(messiness[i], first_j + remaining_spaces**2)
    return messiness[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
