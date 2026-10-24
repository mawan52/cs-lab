#ifndef MAIN_H
#define MAIN_H

typedef struct Node {
    int value;
    int count;
    struct Node* left;
    struct Node* right;
}   node_t;

typedef struct bst {
    node_t* root;
}   bst_t;

bst_t* createTree();
node_t* createNode(int value);

node_t* insert(bst_t* bst, int value);
node_t* search(bst_t* bst, int value);

void freeTree(bst_t* bst);

void preorder(bst_t* bst);
void inorder(bst_t* bst);
void postorder(bst_t* bst);


#endif