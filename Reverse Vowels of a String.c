#define isVowel(x) (x == 'o' || x == 'a' || x == 'e' || x == 'i' || x == 'u' || x == 'O' || x == 'A' || x == 'E' || x == 'I' || x == 'U')

char* reverseVowels(char* s) {
    int i = 0, j = strlen(s) - 1;
    while (i < j) {
        while (i < strlen(s) && !isVowel(s[i])) {
            ++i;
        }
        while (j >= 0 && !isVowel(s[j])) {
            --j;
        }
        if (i < j) {
            s[i] ^= s[j];
            s[j] ^= s[i];
            s[i] ^= s[j];
        }
        ++i, --j;
    }
    return s;
}
