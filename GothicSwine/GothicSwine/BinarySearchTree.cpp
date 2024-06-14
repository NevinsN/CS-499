#include <iostream>

#include "BinarySearchTree.h", "Item.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * Class definitions to handle BinarySearchTrees
 *****************************************************************************************************/

/******************************************************************************************
 * Default constructor for Node
 *****************************************************************************************/
BinarySearchTree::Node::Node() {
	this->left = nullptr;
	this->right = nullptr;
}

/******************************************************************************************
 * Constructor with Item parameter for Node
 *****************************************************************************************/
BinarySearchTree::Node::Node(Item item) {
	Node(); 
	this->item = item;
}

/******************************************************************************************
 * Default constructor for BinarySearchTree
 *****************************************************************************************/
BinarySearchTree::BinarySearchTree() {
	this->root = nullptr;
}

/******************************************************************************************
 * Destructor
 *****************************************************************************************/
BinarySearchTree::~BinarySearchTree() {}

/******************************************************************************************
 * Getter for the root node, should it be necessary
 *****************************************************************************************/
BinarySearchTree::Node* BinarySearchTree::getRootNode() { return this->root; }

/******************************************************************************************
 * Method to traverse the left branch, the root, then the right branch
 *****************************************************************************************/
void BinarySearchTree::inOrder(Node* rootNode) {
    if (rootNode != nullptr) {
        //InOrder not left
        inOrder(rootNode->left);

        std::cout << rootNode->item.getFullItemDescription() << std::endl;

        //InOder right
        inOrder(rootNode->right);
    }
}

/******************************************************************************************
 * Method to traverse the root, the left branch, then the right branch
 *****************************************************************************************/
void BinarySearchTree::preOrder(Node* rootNode) {
    if (rootNode != nullptr) {
        //output bidID, title, amount, fund
        std::cout << rootNode->item.getFullItemDescription() << std::endl;

        //postOrder left
        postOrder(rootNode->left);

        //postOrder right
        postOrder(rootNode->right);
    }
}

/******************************************************************************************
 * Method to traverse the left branch, the right branch, then the root
 *****************************************************************************************/
void BinarySearchTree::postOrder(Node* rootNode) {
    if (rootNode != nullptr) {
        //postOrder left
        postOrder(rootNode->left);

        //postOrder right
        postOrder(rootNode->right);

        //output bidID, title, amount, fund
        std::cout << rootNode->item.getFullItemDescription() << std::endl;
    }
}

/******************************************************************************************
 * Method to add a node to the BST
 *****************************************************************************************/
void BinarySearchTree::insertNode(Node* rootNode, Item item) {
    if (rootNode->item.getItemID() > item.getItemID()) {
        // if no left node
        if (rootNode->left == nullptr) {
            // this node becomes left
            rootNode->left = new Node(item);
        }
        // else recurse down the left node
        else {
            this->insertNode(rootNode->left, item);
        }
    }
    // else
    else {
        // if no right node
        if (rootNode->right == nullptr) {
            // this node becomes right
            rootNode->right = new Node(item);
        }
        //else
        else {
            // recurse down the left node
            this->insertNode(rootNode->right, item);
        }
    }
}

/******************************************************************************************
 * Method to remove a node from the BST
 *****************************************************************************************/
void BinarySearchTree::removeNode(Node* rootNode) {
// FIXME: Implement removeNode()
}

/******************************************************************************************
 * Method to find an item in the BST by itemID
 *****************************************************************************************/
Item BinarySearchTree::getItemByID(int itemID) {
    Node* currentNode = root;

    // keep looping downwards until bottom reached or matching bidId found
    while (currentNode != nullptr) {
        // if match found, return current bid
        if (currentNode->item.getItemID() == itemID) {
            return currentNode->item;
        }
        // if bid is smaller than current node then traverse left
        if (itemID < currentNode->item.getItemID()) {
            currentNode = currentNode->left;
        }
        // else larger so traverse right
        else {
            currentNode = currentNode->right;
        }
    }

    Item item;
    return item;
}