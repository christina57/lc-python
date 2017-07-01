def numberOfPatterns(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    #[[0] * 10] * 10  #
    jump = [[0 for j in range(10)] for i in range(10)]
    jump[1][3] = jump[3][1] = 2
    jump[1][7] = jump[7][1] = 4
    jump[3][9] = jump[9][3] = 6
    jump[7][9] = jump[9][7] = 8
    jump[2][8] = jump[8][2] = jump[4][6] = jump[6][4] = jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5
    used = [False] * 10
    res = 0
    for k in range(m, n + 1):
        res += dfs(1, k - 1, jump, used) * 4
        res += dfs(2, k - 1, jump, used) * 4
        res += dfs(5, k - 1, jump, used)

    return res


def dfs(start, remain, jump, used):
    if remain == 0:
        return 1

    used[start] = True
    res = 0

    for i in range(1, 10):
        if (not used[i]) and (jump[start][i] == 0 or used[jump[start][i]]):
            res += dfs(i, remain - 1, jump, used)

    used[start] = False
    return res

print numberOfPatterns(2,2)