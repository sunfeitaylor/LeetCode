class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mul = int(num1[i]) * int(num2[j])
                mul_sum = mul + res[i + j + 1]
                res[i + j + 1] = mul_sum % 10
                res[i + j] += mul_sum // 10
        res = "".join(map(str, res))
        return '0' if not res.lstrip("0") else res.lstrip("0")


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {}
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                d[i + j] = d.get(i + j, 0) + int(n1) * int(n2)
        for k in range(len(d)):
            d[k + 1] = d.get(k + 1, 0) + d[k] // 10
            d[k] = d[k] % 10
        return re.sub('^0*', '', ''.join(map(str, d.values()))[::-1]) or '0'
