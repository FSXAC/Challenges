def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    def match(c):
        a = '({['
        b = ')}]'
        return a[b.index(c)]
    
    stack = []
    
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')]}':
            if len(stack) == 0:
                return False
            last = stack[len(stack) - 1]
            if last == match(c):
                stack.pop()
            else:
                return False
    
    return len(stack) == 0