class Solution:
    def longestValidParentheses(self, string):
        stack=[-1]
        answer=0
        for i,ch in enumerate(string):
            if ch=='(':
                stack.append(i)
            else:
                if len(stack)>1:
                    stack.pop()
                    answer=max(answer,i-stack[-1])
                else:
                    stack[-1]=i
        return answer

ins=Solution()

print ins.longestValidParentheses("()(()")