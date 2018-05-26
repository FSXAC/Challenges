def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    out = x % 10
    while x > 0:
        out *= 10
        out += x
        x // 10

    return out

print(reverse(12345))