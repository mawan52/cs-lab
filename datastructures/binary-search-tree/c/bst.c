#include "bst.h"

#include <stdlib.h>
#include <stdio.h>

node_t *createNode(int value)
{
    node_t *node = malloc(sizeof(node_t));
    if (NULL == node) return NULL;
    node->value = value;
    node->count = 1;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void freeTree(node_t *root)
{
    if (NULL == root);
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

node_t *insert(node_t *root, int value)
{
    if (root == NULL)
        return createNode(value);

    if (value < root->value)
    {
        root->left = insert(root->left, value);
    }
    else if (value > root->value)
    {
        root->right = insert(root->right, value);
    }
    else
    {
        root->count++;
    }

    return root;
}

node_t *search(node_t *root, int value)
{
    if (root == NULL || root->value == value)
        return root;

    if (value < root->value)
    {
        return search(root->left, value);
    }
    return search(root->right, value);
}

// root to bottom
void preorder(node_t *root)
{
    if (NULL == root)
        return;
    printf("%d\n", root->value);
    preorder(root->left);
    preorder(root->right);
}

// left to right
void inorder(node_t *root)
{
    if (NULL == root)
        return;
    inorder(root->left);
    printf("%d\n", root->value);
    inorder(root->right);
}

// bottom to up
void postorder(node_t *root)
{
    if (NULL == root)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d\n", root->value);
}