class Solution(object):
    def findContentChildren(self, g, s):
        counter = 0
        g.sort()
        s.sort()
        g_ptr, s_ptr = 0, 0
        g_size, s_size = len(g), len(s)
        while g_ptr < g_size and s_ptr < s_size:
            current_g = g[g_ptr]
            while s_ptr < s_size and s[s_ptr] < current_g:
                s_ptr += 1
            if s_ptr == s_size:
                break
            counter += 1
            g_ptr += 1
            s_ptr += 1
        return counter
