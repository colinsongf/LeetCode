class Solution(object):
    def addStrings(self, num1, num2):
        while len(num1) < len(num2):
            num1 = '0' + num1
        while len(num2) < len(num1):
            num2 = '0' + num2
        i, j = len(num1) - 1, len(num2) - 1
        jw = 0
        answer = []
        while i >= 0 and j >= 0:
            sub = int(num1[i]) + int(num2[j]) + jw
            jw = sub / 10
            sub = sub % 10
            answer.append(str(sub))
            i -= 1
            j -= 1
        if jw:
            answer.append(str(jw))
        answer.reverse()
        return ''.join(answer)
