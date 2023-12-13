from typing import List

class TreeNode:
    # forward reference class TreeNode as it has not been defined yet
    parent: 'TreeNode' = None
    # Left child
    left: 'TreeNode' = None
    # Right child
    right: 'TreeNode' = None
    # The actual value stored in the node
    val: int = None
    # The depth of the node in the tree. Root has depth of 0.
    depth: int = 0
    
    
    def __init__(self, node_numbers: List[int], parent: 'TreeNode' = None) -> 'TreeNode':
        """Constructs a TreeNode from a list of integers.

        Args:
            node_numbers (List[int]): Sorted, unique list of integers to construct a `TreeNode` from.
            parent (TreeNode, optional): Parent node to set on this `TreeNode`. Defaults to None.

        Returns:
            TreeNode: The root node of the constructed tree.
        """
        
        # No integers are left. This means the parent node is a leaf node.
        if len(node_numbers) == 0:
            raise ValueError("Cannot construct a tree from an empty list of integers.")
        
        # Get the middle index of the list of integers
        root_index = len(node_numbers) // 2
        root_node_number = node_numbers[root_index]
        
        # Split the list of integers into two halves
        left_subtree = node_numbers[:root_index]
        right_subtree = node_numbers[root_index + 1:]
        
        self.val = root_node_number
        self.parent = parent
        self.depth = parent.depth + 1 if parent is not None else 0
        
        # Recursively construct the left and right subtrees
        self.left = TreeNode(left_subtree, self) if len(left_subtree) > 0 else None
        self.right = TreeNode(right_subtree, self) if len(right_subtree) > 0 else None
        
    @staticmethod
    def equals(a: 'TreeNode', b: 'TreeNode') -> bool:
        """Returns whether two treenodes are equal

        Returns:
            bool: Whether these two treenodes are exactly equal
        """
        
        # Since we assume that all node values are unique, all we need to know is whether the values are equal
        return a.val == b.val
    
    def preprocess_val_for_report(self, val: int) -> str:
        """Preprocesses a value for printing in the report.

        Args:
            val (int): The value to preprocess.

        Returns:
            str: The preprocessed value.
        """
        retVal = str(val)
        
        # Surround negative values in parentheses
        if val < 0:
            retVal = f"({retVal})"
        
        return retVal
    def print_report(self, depth = 0):
        """Prints the node and its descendants in pre-order traversal.

        Args:
            depth (int, optional): Depth of the printed report. 
                The first level of the report will include a short description of report format.
                Defaults to 0.
        """
        if (depth == 0):
            print("Printing tree of cardinality " + str(len(self.descendants()) + 1) + " in pre-order traversal.")
            print("At each level, the left node is printed first, then the right node.")
            
        # Add some lines to the front of the string to indicate the depth of the node
        prefix_tree_lines = '-' * self.depth * 2
        
        # printed string starts off with the prefix tree lines and the value of the node
        print_str = F"{prefix_tree_lines}{self.preprocess_val_for_report(self.val)}"
        
        # Add some subtext to the printed string to indicate if the node is the root or a leaf
        if (self.is_root()):
            print_str += "\t(ROOT)"
            
        if not self.is_root():
            if TreeNode.equals(self, self.parent.left):
                print_str += "\t(LEFT CHILD)"
            elif TreeNode.equals(self, self.parent.right):
                print_str += "\t(RIGHT CHILD)"
            if len(self.parent.children()) == 1:
                print_str += "\t(ONLY CHILD)"
                
        if self.is_leaf():
            print_str += "\t(LEAF)"
            
        print(print_str)
        
        # Print children recursively
        for child in self.children():
            child.print_report(depth + 1)

    def is_root(self) -> bool:
        """Returns whether this node is the root of the tree.

        Returns:
            bool: Whether this node is a tree root (has no parent)
        """
        return self.parent is None
    
    def is_leaf(self) -> bool:
        """Returns whether this node is a leaf node (has no children).

        Returns:
            bool: Whether this node is a leaf node
        """
        return len(self.children()) == 0

    def children(self) -> List['TreeNode']:
        """Returns a list of the children of this node.

        Returns:
            _type_: All children of this node.
        """
        return [node for node in [self.left, self.right] if node is not None]
    
    def ancestors(self) -> List['TreeNode']:
        """Returns a list of all ancestors (parent, grandparent, etc.) of this node.

        Returns:
            _type_: All ancestors of this node.
        """
        retVal = []
        if self.is_root():
            return retVal
        
        retVal.append(self.parent)
        retVal.extend(self.parent.ancestors())
            
        return retVal

    def descendants(self) -> List['TreeNode']:
        """Returns a list of all descendants (children, children's children, etc.) of this node.

        Returns:
            _type_: All descendants of this node.
        """
        retVal = []
        for child in self.children():
            retVal.append(child)
            retVal.extend(child.descendants())

        return retVal
    
    def search(self, val: int) -> 'TreeNode':
        """Searches the tree for a node with the given value.

        Args:
            val (int): Value to search for.

        Returns:
            TreeNode: Node with `val`=`val`, if found. Else, `None`.
        """
        
        assert self is not None, "Cannot search a null tree."
        
        # Base case 1: This node has the value we're looking for! Return it.
        if self.val == val:
            return self
        
        # Base case 2: This node is a leaf node. This branch of the search is over, return None.
        if self.is_leaf():
            return None
        
        # Decide on left or right subtree based on numeric comparison
        subtree = self.left if val < self.val else self.right
        
        # If the subtree is None and we've gotten this far, the node only has one child, but that child mathematically cannot have the value we're looking for.
        # So the value is not in the tree.
        if subtree is None:
            return None
        
        # Recursive case: Search the appropriate subtree
        return subtree.search(val)