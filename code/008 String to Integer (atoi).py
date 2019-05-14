# This solution scan the str from start to end to find the proper (i, j) index.
# maybe str[i].isdigit() is a better way than str[i] in '0123456789'
class Solution:
    def myAtoi(self, str: str) -> int:
        n = len(str)
        if not n:
            return 0
        for i in range(n):
            if str[i] != ' ':
                break
        if str[i] not in '+-0123456789':
            return 0
        elif i == n - 1:
            if str[i] in '+-':
                return 0
            else:
                return int(str[i])
        else:
            for j in range(i + 1, n):
                if str[j] not in '0123456789':
                    break
            if j == n - 1 and str[j] in '0123456789':
                res = int(str[i:])
            elif j == i + 1 and str[i] not in '0123456789':
                return 0
            else:
                res = int(str[i: j])
            if res < 2 ** 31 - 1:
                if res > - 2 ** 31:
                    return res
                else:
                    return -2 ** 31
            else:
                return 2 ** 31 - 1
