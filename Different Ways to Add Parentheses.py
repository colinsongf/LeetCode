class Solution:
    def calcArr(self, arr1, arr2, op):
        answer = []
        for n1 in arr1:
            for n2 in arr2:
                subans = n1 + n2 if op == '+' else n1 - n2 if op == '-' else n1 * n2
                answer.append(subans)
        return answer

    def diffWaysToCompute(self ,input):
        numbers = [int(x) for x in re.split('[+*-]',input)]
        ops = []
        for ch in input:
            if ch in '+-*':
                ops.append(ch)
        size = len(numbers)
        m = [[None for y in range(size)] for x in range(size)]
        for i in range(size):
            m[i][i] = [numbers[i]]
        for l in range(2, size + 1):
            for i in range(size - l + 1):
                j = i + l - 1
                m[i][j] = []
                for k in range(i,j):
                    m[i][j].extend(self.calcArr(m[i][k], m[k + 1][j], ops[k]))
        return  sorted(m[0][size - 1])