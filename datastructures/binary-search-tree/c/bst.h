/*
A Binary Search Tree (BST) is a special type of
Binary Tree that follows an ordering rule:
-   All values in the left subtree are smaller
    than the value of the current node.

-   All values in the right subtree are
    greater than the value of the current node.
*/

#ifndef BST_H
#define BST_H

typedef struct Node
{
    int value;
    int count;
    struct Node *left;
    struct Node *right;
} node_t;

node_t *createNode(int value);

node_t *insert(node_t *root, int value);
node_t *search(node_t *root, int value);

void freeTree(node_t *root);

void preorder(node_t *root);
void inorder(node_t *root);
void postorder(node_t *root);

#endif // BST_H