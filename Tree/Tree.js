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
    _insert (value) {
        if (this.root === null) {
            this.root = new TreeNode(value);
        } else {
            this._insertNode(value, this.root);
        }
    }
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
    _printTreeBrackets () {
        console.log(this._printNode(this.root));
    }
    // takes a node and prints it's val and then recursively 
    // deals with subsequent levels
    _printNode (node) {
        return `(${node.value}: ${node.left ? this._printNode(node.left) : ""}, ${node.right ? this._printNode(node.right) : ""})`;
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

binaryTree.printTree();