def matrixReshape(nums, r, c):
    if len(nums) == 0:
        return [[]]
    if len(nums[0]) == 0:
        return [[]]

    elements = len(nums) * len(nums[0])

    if elements != (r * c):
        # can't reshape
        return nums

    es = []
    for row in nums:
        for e in row:
            es.append(e)

    out = []
    for ri in range(r):
        out.append([])
        for ci in range(c):
            out[ri].append(es[ri * c + ci])

    return out

print(matrixReshape([[1,2],[3,4]], 1, 4))