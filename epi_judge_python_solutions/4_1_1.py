# Right propagate the rightmost set bit in x (01010000)2 becomes (01011111)2

def right_propagate(x):
    return x | (x-1)

assert right_propagate(0b01010000) == 0b01011111


# X mod a power of two 77 mod 64 = 13

def mod_power2(x, power2):
    return x & (power2 - 1)

assert mod_power2(77, 64) == 13

# Is power of 2
def is_power2(x):
    return not x & (x-1)

assert is_power2(1)
assert is_power2(2)

assert not is_power2(3)
