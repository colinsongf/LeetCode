class Solution(object):
    def lexicalOrder(self, n):
        answer = []
        if n < 1:
            return answer
        answer = [1]
        while len(answer) < n:
            number = answer[-1]
            if number * 10 <= n:
                answer.append(number * 10)
            else:
                if number % 10 == 9:
                    next = number + 1
                    while next % 10 == 0:
                        next /= 10
                    if next <= n:
                        answer.append(next)
                elif number + 1 <= n:
                    answer.append(number + 1)
                else:
                    answer.append(number / 10 + 1)
        return answer
