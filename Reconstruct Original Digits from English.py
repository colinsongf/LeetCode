class Solution(object):
    def originalDigits(self, s):
        counter = {}
        answer_counter = {}
        for ch in s:
            counter[ch] = 1 if ch not in counter else (counter[ch] + 1)
        answer = ''
        #handle 0: z is unique
        zero_cnt = counter['z'] if 'z' in counter else 0
        answer_counter[0] = zero_cnt
        if zero_cnt:
            answer_counter[0] = zero_cnt
            del counter['z']
            counter['e'] -= zero_cnt
            if not counter['e']:
                del counter['e']
            counter['r'] -= zero_cnt
            if not counter['r']:
                del counter['r']
            counter['o'] -= zero_cnt
            if not counter['o']:
                del counter['o']
        #handle 2
        two_cnt = counter['w'] if 'w' in counter else 0
        answer_counter[2] = two_cnt
        if two_cnt:
            del counter['w']
            counter['t'] -= two_cnt
            if not counter['t']:
                del counter['t']
            counter['o'] -= two_cnt
            if not counter['o']:
                del counter['o']
        #handle 4
        four_cnt = counter['u'] if 'u' in counter else 0
        answer_counter[4] = four_cnt
        if four_cnt:
            del counter['u']
            counter['f'] -= four_cnt
            if not counter['f']:
                del counter['f']
            counter['o'] -= four_cnt
            if not counter['o']:
                del counter['o']
            counter['r'] -= four_cnt
            if not counter['r']:
                del counter['r']
        #handle 6
        six_cnt = counter['x'] if 'x' in counter else 0
        answer_counter[6] = six_cnt
        if six_cnt:
            del counter['x']
            counter['s'] -= six_cnt
            if not counter['s']:
                del counter['s']
            counter['i'] -= six_cnt
            if not counter['i']:
                del counter['i']
        #handle 8
        eight_cnt = counter['g'] if 'g' in counter else 0
        answer_counter[8] = eight_cnt
        if eight_cnt:
            del counter['g']
            counter['e'] -= eight_cnt
            if not counter['e']:
                del counter['e']
            counter['i'] -= eight_cnt
            if not counter['i']:
                del counter['i']
            counter['h'] -= eight_cnt
            if not counter['h']:
                del counter['h']
            counter['t'] -= eight_cnt
            if not counter['t']:
                del counter['t']
        #handle 1, 3, 5, 7, 9
        #handle 1
        one_cnt = counter['o'] if 'o' in counter else 0
        answer_counter[1] = one_cnt
        if one_cnt:
            del counter['o']
            counter['n'] -= one_cnt
            if not counter['n']:
                del counter['n']
            counter['e'] -= one_cnt
            if not counter['e']:
                del counter['e']
        #handle 3
        three_cnt = counter['h'] if 'h' in counter else 0
        answer_counter[3] = three_cnt
        if three_cnt:
            del counter['h']
            counter['t'] -= three_cnt
            if not counter['t']:
                del counter['t']
            counter['e'] -= (three_cnt * 2)
            if not counter['e']:
                del counter['e']
            counter['r'] -= three_cnt
            if not counter['r']:
                del counter['r']
        #handle 5
        five_cnt = counter['f'] if 'f' in counter else 0
        answer_counter[5] = five_cnt
        if five_cnt:
            del counter['f']
            counter['i'] -= five_cnt
            if not counter['i']:
                del counter['i']
            counter['e'] -= five_cnt
            if not counter['e']:
                del counter['e']
            counter['v'] -= five_cnt
            if not counter['v']:
                del counter['v']
        #handle 7
        sve_cnt = counter['s'] if 's' in counter else 0
        answer_counter[7] = sve_cnt
        if sve_cnt:
            del counter['s']
            counter['v'] -= sve_cnt
            if not counter['v']:
                del counter['v']
            counter['e'] -= (sve_cnt * 2)
            if not counter['e']:
                del counter['e']
            counter['n'] -= sve_cnt
            if not counter['n']:
                del counter['n']
        #handle 9
        nine_cnt = counter['i'] if 'i' in counter else 0
        answer_counter[9] = nine_cnt

        for i in range(10):
            if answer_counter[i]:
                answer += (answer_counter[i] * str(i))
        return answer
