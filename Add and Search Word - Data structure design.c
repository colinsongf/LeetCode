struct WordDictionary {
	struct WordDictionary *childs[26];
	bool isLeaf;
};

/** Initialize your data structure here. */
struct WordDictionary* wordDictionaryCreate() {
	int i;
	struct WordDictionary *node=malloc(sizeof(struct WordDictionary));
	if(!node)
		exit(1);
	for(i=0;i<26;++i)
		node->childs[i]=NULL;
	node->isLeaf=false;
	return node;
}

/** Inserts a word into the data structure. */
void addWord(struct WordDictionary* wordDictionary, char* word) {
	struct WordDictionary *current=wordDictionary;
	while(*word){
		if(!current->childs[*word-'a'])
			current->childs[*word-'a']=wordDictionaryCreate();
		current=current->childs[*word-'a'];
		word++;
	}
	current->isLeaf=true;
}

/** Returns if the word is in the data structure. A word could
    contain the dot character '.' to represent any one letter. */
bool search(struct WordDictionary* wordDictionary, char* word) {
	if(!wordDictionary)
		return false;
	if(*word=='\0')
		return wordDictionary->isLeaf;
	if(*word>='a' && *word<='z')
		return search(wordDictionary->childs[*word-'a'],word+1);
	int i;
	for(i=0;i<26;++i)
		if(search(wordDictionary->childs[i],word+1))
			return true;
	return false;
}

/** Deallocates memory previously allocated for the data structure. */
void wordDictionaryFree(struct WordDictionary* wordDictionary) {
	if(!wordDictionary)
		return ;
	int i;
	for(i=0;i<26;++i)
		wordDictionaryFree(wordDictionary->childs[i]);
	free(wordDictionary);
}