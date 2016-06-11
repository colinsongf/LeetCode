char* reverseString(char* s) {
    int i = 0, j = strlen(s) - 1;
    while (i < j) {
        s[i] ^= s[j];
        s[j] ^= s[i];
        s[i] ^= s[j];
        ++i, --j;
    }
    return s;
}
