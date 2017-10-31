def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    return ((num ** (1/4)) % 1 == 0)

print(isPowerOfFour(4))