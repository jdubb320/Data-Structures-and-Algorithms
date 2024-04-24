# Trees and Graphs

## Trees

### Types of Trees

_Binary tree_: each node as up to 2 children; no more than 2

_Leaf_: a node with no children

_Binary search tree_: a binary tree in which every node fits a specific ordering property (i.e all left descendants <= n < all right)

_Balanced tree_: "more like not terribly unbalanced"; balanced enough to ensure O(log n) times for insert/find

_Complete binary trees_: every level of the tree if fully filled, except for perhaps the last level, in which case the last level is filled left to right (i.e. the child is to the left and NOT right of the last level)

_Full binary tree_: each node has either 0 or 2 children, no node has 1 child

_Perfect binary tree_: all interior nodes have 2 children and all leaf nodes are at the same level (rare in real-life and interviews)

### Binary Tree Traversal

**In-Order traversal** (most common): means to "visit" the left branch, then current node, finally the right branch; when performed in a Binary Search Tree, it visits the nodes in ascending order (hence "in-order")

```c++
void inOrderTraversal(TreeNode node){
    if (node != null) {
        inOrderTraversal(node.left);
        visit(node);
        inOrderTraversal(node.right);
    }
}
```

**Pre-Order traversal**: visits the current node before its child nodes (hence "pre-order"); root is always the first node visited

```c++
void preOrderTraversal(TreeNode node){
    if (node != null) {
        visit(node);
        preOrderTraversal(node.left);
        preOrderTraversal(node.right);
    }
}
```

**Post-Order traversal**: visits current node _after_ its children (hence "post-order"); root is always the _last_ node visited

```c++
void preOrderTraversal(TreeNode node){
    if (node != null) {
        visit(node);
        preOrderTraversal(node.left);
        preOrderTraversal(node.right);
    }
}
```

### Binary Heaps (Min-Heaps and Max-Heaps)

It discussed only min-heaps since max-heaps are essentially the same _but_ elements are in descending order rather than ascending order.

**Min-heap**: a _complete_ binary tree where each node is smaller than its children making the root the smallest element in the tree