def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False

    original = x

    rev = 0
    while x != 0:
        rev *= 10
        rev += x % 10
        x = x // 10

    print(rev)
    return rev == original


while True:
    print(isPalindrome(int(input())))
