bool isAnagram(char* s, char* t) {
    int ssize = strlen(s),tsize = strlen(t);
    int hashmap[26] = {};
    int i;
    for (i = 0;i < ssize; ++i)
        hashmap[s[i] - 'a']++;
    for (i = 0;i < tsize; ++i) {
        if (hashmap[t[i] - 'a'] == 0)
            return false;
        hashmap[t[i] - 'a']--;
    }
    for (i = 0;i < 26; ++i)
        if (hashmap[i] != 0)
            return false;
    return true;
}