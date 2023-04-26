class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null
    }
    // handles putting in the root node and every subsequent
    // node
    _insert (value) {
        if (this.root === null) {
            this.root = new TreeNode(value);
        } else {
            this._insertNode(value, this.root);
        }
    }
    // handles recursion of finding the place where the new node
    // will be and puts it in
    _insertNode (value, node) {
        if (value >= node.value) {
            // it's going right
            if (node.right) {
                this._insertNode(value, node.right); 
            } else {
                node.right = new TreeNode(value);
            }
        } else {
            // it's going left
            if (node.left) {
                this._insertNode(value, node.left); 
            } else {
                node.left = new TreeNode(value);
            }
        }
    }
    // prints the tree in a human readable format
    _printTree () {
        console.log(this._printNode(this.root));
    }
    // takes a node and prints it's val and then recursively 
    // deals with subsequent levels
    _printNode (node) {
        return `(${node.value}: ${node.left ? this._printNode(node.left) : ""}, ${node.right ? this._printNode(node.right) : ""})`;
    }

    // implementing pre-order tree traversal
    // starts with root, goes left, then right
    preOrderTraversal() {
        const result = [];
        this._preOrderTraversalHelper(this.root, result);
        console.log(result);
      }
    
    _preOrderTraversalHelper(node, list) {
        if (node) {
            list.push(node.value);
            this._preOrderTraversalHelper(node.left, list);
            this._preOrderTraversalHelper(node.right, list);
        }
    }
    // Implementing in-order tree traversal,
    // starts with left, then back to root then right.
    // Interesting property is that this gets us the nodes 
    // in order of size.
    inOrderTraversal() {
        const result = [];
        this._inOrderTraversalHelper(this.root, result);
        console.log(result);
    }
    _inOrderTraversalHelper(node, list) {
        if (node) {
            this._inOrderTraversalHelper(node.left, list);
            // after evaluatijng everything below and left, add node
            list.push(node.value);
            // then search the right
            this._inOrderTraversalHelper(node.right, list);
        }
    }
    // goes left, right , root
    postOrderTraversal() {
        const result = [];
        this._postOrderTraversalHelper(this.root, result);
        console.log(result);
    }
    _postOrderTraversalHelper(node, list) {
        if (node) {
            this._postOrderTraversalHelper(node.left, list);
            this._postOrderTraversalHelper(node.right, list);
            // only adding the root when both branches visited
            list.push(node.value);

        }
    }
}
const binaryTree = new BinaryTree();
binaryTree._insert(50);
binaryTree._insert(60);
binaryTree._insert(40);
binaryTree._insert(45);
binaryTree._insert(70);
binaryTree._insert(75);
binaryTree._insert(77);
binaryTree._insert(30);
binaryTree._insert(55);

binaryTree.inOrderTraversal();