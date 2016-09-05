class Solution:
    def toTokens(self, s):
        tokens = []
        n = 0
        for ch in s:
            if ch == '[':
                tokens.append(n)
                n = 0
            elif ch in '0123456789':
                n *= 10
                n += int(ch)
            else:
                tokens.append(ch)
        return tokens

    def decodeString(self, s):
        tokens = self.toTokens(s)
        int_stack = []
        string_stack = []
        final_string = ''
        for token in tokens:
            if type(token) == int:
                int_stack.append(token)
                string_stack.append('@')
            elif token == ']':
                string = string_stack.pop()
                integer = int_stack.pop()
                new_string = ''.join(string for i in range(integer))
                if not int_stack:
                    final_string += new_string
                elif string_stack[-1] == '@':
                    string_stack[-1] = new_string
                else:
                    string_stack[-1] += new_string
            else:
                if not int_stack:
                    final_string += token
                elif string_stack[-1] == '@':
                    string_stack[-1] = token
                else:
                    string_stack[-1] += token
        return final_string
