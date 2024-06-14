#pragma once

#include "Item.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * A class header to handle creation of BinarySearchTrees for items
 *****************************************************************************************************/

class BinarySearchTree {
	// Item Structure for the BST Nodes
	struct Node {
		Item item;
		Node* left;
		Node* right;

		// Default Constructor
		Node();

		// Constructor with item
		Node(Item item);
	};

	Node* root;

public:
	// Constructor and Destructor
	BinarySearchTree();
	~BinarySearchTree();

	// Getters
	Node* getRootNode();
	Item getItemByID(int itemID);

	// Traversal and Adding/Removing Methods
	void inOrder(Node* rootNode);
	void preOrder(Node* rootNode);
	void postOrder(Node* rootNode);
	void insertNode(Node* rootNode, Item item);
	void removeNode(Node* rootNode);
};