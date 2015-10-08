#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TrieNode {
	char isLeaf;
	struct TrieNode *childs[26];
};

/** Initialize your data structure here. */
struct TrieNode* trieCreate() {
	int i;
	struct TrieNode *root=(struct TrieNode *)malloc(sizeof(struct TrieNode));
	if(!root)
		exit(1);
	memset(root,0,sizeof(struct TrieNode));
	return root;
}

/** Inserts a word into the trie. */
void insert(struct TrieNode* root, char* word) {
	struct TrieNode *current=root;
	while(*word){
		if(!current->childs[*word-'a'])
			current->childs[*word-'a']=trieCreate();
		current=current->childs[*word-'a'];
		word++;
	}
	current->isLeaf=1;
}

/** Returns if the word is in the trie. */
bool search(struct TrieNode* root, char* word) {
    struct TrieNode *current=root;
    while(*word){
    	if(!current->childs[*word-'a'])
    		return false;
    	current=current->childs[*word-'a'];
    	word++;
    }
    return current->isLeaf==1?true:false;
}

/** Returns if there is any word in the trie 
    that starts with the given prefix. */
bool startsWith(struct TrieNode* root, char* prefix) {
    struct TrieNode *current=root;
    while(*prefix!='\0'){
    	if(!current->childs[*prefix-'a'])
    		return false;
    	current=current->childs[*prefix-'a'];
    	prefix++;
    }
    return true;
}

/** Deallocates memory previously allocated for the TrieNode. */
void trieFree(struct TrieNode* root) {
    if(!root)
    	return ;
    int i;
    for(i=0;i<26;++i)
    	if(root->childs[i])
    		trieFree(root->childs[i]);
    free(root);
}

// Your Trie object will be instantiated and called as such:
// struct TrieNode* node = trieCreate();
// insert(node, "somestring");
// search(node, "key");
// trieFree(node);