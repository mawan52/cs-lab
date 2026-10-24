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

node_t* createNode(int value);

node_t* insert(node_t* root, int value);
node_t* search(node_t* root, int value);

void freeTree(node_t* root);

void preorder(node_t* root);
void inorder(node_t* root);
void postorder(node_t* root);


#endif