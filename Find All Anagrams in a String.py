def hash_equal(hash1, hash2):
    if len(hash1) != len(hash2):
        return False
    for key in hash1:
        if key not in hash2 or hash2[key] != hash1[key]:
            return False
    return True

class Solution(object):
    def findAnagrams(self, s, p):
        answer = []
        phash = {}
        for ch in p:
            if ch not in phash:
                phash[ch] = 1
            else:
                phash[ch] += 1
        window_size = len(p)
        total_size = len(s)
        if total_size < window_size:
            return answer
        subhash = {}
        for ch in s[:window_size]:
            if ch not in subhash:
                subhash[ch] = 1
            else:
                subhash[ch] += 1
        i, j = 0, window_size - 1
        while i < total_size and j < total_size:
            if hash_equal(subhash, phash):
                answer.append(i)
            delete = s[i]
            if j + 1>= total_size:
                break
            add = s[j + 1]
            if add not in subhash:
                subhash[add] = 1
            else:
                subhash[add] += 1
            if subhash[delete] == 1:
                del subhash[delete]
            else:
                subhash[delete] -= 1
            i += 1
            j += 1
        return answer
