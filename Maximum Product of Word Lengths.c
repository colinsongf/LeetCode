int createBitMap(char *word) {
    int bit = 0;
    while (word && *word != '\0') {
        bit |= (1 << (*word - 'a'));
        ++word;
    }
    return bit;
}

#define HasNoSame(a, b) (((a) & (b)) == 0)

int maxProduct(char **words, int wordsSize) {
    int bitmaps[wordsSize];
    int i, j, max = 0;
    for (i = 0;i < wordsSize; ++i) {
        bitmaps[i] = createBitMap(words[i]);
    }
    for (i = 0;i < wordsSize - 1; ++i) {
        for (j = i + 1;j < wordsSize; ++j) {
            if (HasNoSame(bitmaps[i], bitmaps[j])) {
                if (strlen(words[i]) * strlen(words[j]) > max) {
                    max = strlen(words[i]) * strlen(words[j]); 
                }
            }
        }
    }
    return max;
}
