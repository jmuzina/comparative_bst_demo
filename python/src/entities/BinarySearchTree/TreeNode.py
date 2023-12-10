from typing import List
from enum import Enum

class NodeRelationship(Enum):
    """Enum representing the relationship of one node to another."""
    PARENT = 0
    LEFT_CHILD = 1
    RIGHT_CHILD = 2
    LEFT_DESCENDANT = 3
    RIGHT_DESCENDANT = 4
    SIBLING = 5
    COUSIN = 6
    AUNT_OR_UNCLE = 7
    ANCESTOR = 8
    OTHER = 9

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
    
    @staticmethod
    def construct_node_from_list(node_numbers: List[int], parent: 'TreeNode' = None) -> 'TreeNode':
        """Recursively constructs a TreeNode from a list of integers.

        Args:
            node_numbers (List[int]): Sorted, unique list of integers to construct a `TreeNode` from.
            parent (TreeNode, optional): Parent node to set on this `TreeNode`. Defaults to None.

        Returns:
            TreeNode: The root node of the constructed tree.
        """
        
        # No integers are left. This means the parent node is a leaf node.
        if len(node_numbers) == 0:
            return None
        
        # Get the middle index of the list of integers
        root_index = len(node_numbers) // 2
        root_node_number = node_numbers[root_index]
        
        # Split the list of integers into two halves
        left_subtree = node_numbers[:root_index]
        right_subtree = node_numbers[root_index + 1:]
        
        # The root node is the middle element of the list of integers.
        retVal = TreeNode(
            val=root_node_number, 
            parent=parent,
            depth=parent.depth + 1 if parent is not None else 0
        )
        
        # Recursively construct the left and right subtrees using the left and right halves of the list of integers
        retVal.left = TreeNode.construct_node_from_list(left_subtree, retVal)
        retVal.right = TreeNode.construct_node_from_list(right_subtree, retVal)
        
        return retVal
    
    @staticmethod
    def equals(a: 'TreeNode', b: 'TreeNode') -> bool:
        """Returns whether two treenodes are equal

        Returns:
            bool: Whether these two treenodes are exactly equal
        """
        
        # Since we assume that all node values are unique, all we need to know is whether the values are equal
        return a.val == b.val
    
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
        print_str = F"{prefix_tree_lines}{str(self.val)}"
        
        # Add some subtext to the printed string to indicate if the node is the root or a leaf
        if (self.is_root()):
            print_str += "\t(ROOT)"
            
        if self.is_leaf():
            print_str += "\t(LEAF)"
            
        print(print_str)
        
        # Print children recursively
        for child in self.children():
            child.print_report(depth + 1)
            
    def relationship_to(self, other: 'TreeNode') -> NodeRelationship:
        """Returns the relationship of this node to another node.

        Args:
            other (TreeNode): The other node to compare this node to.

        Returns:
            str: The relationship of this node to the other node.
        """
        
        if not self.is_root() and not other.is_root():
            if TreeNode.equals(self.parent, other.parent):
                return NodeRelationship.SIBLING
            elif other.relationship_to(self.parent) == NodeRelationship.SIBLING:
                return NodeRelationship.AUNT_OR_UNCLE
            elif other.parent.relationship_to(self.parent) == NodeRelationship.SIBLING:
                return NodeRelationship.COUSIN
        
        if not other.is_root():
            if TreeNode.equals(self, other.parent):
                return NodeRelationship.PARENT
            
        if not self.is_root():
            if TreeNode.equals(self.parent, other):
                if TreeNode.equals(self, other.left):
                    return NodeRelationship.LEFT_CHILD
                elif TreeNode.equals(self, other.right):
                    return NodeRelationship.RIGHT_CHILD
                else:
                    # This is a handy way of testing that the tree structure is constructed correctly.
                    raise Exception(f"Node {self.val}'s parent is {other.val}, but {other.val} does not have {self.val} as a child.")
            # `other` is not a direct parent of `self`, but could be an ancestor
            else:
                for ancestor in self.ancestors():
                    if TreeNode.equals(other, ancestor):
                        if self.val < other.val:
                            return NodeRelationship.LEFT_DESCENDANT
                        # if not less than, must be greater than. assumes values are unique
                        return NodeRelationship.RIGHT_DESCENDANT
        
        for descendant in self.descendants():
            if TreeNode.equals(self, descendant):
                return NodeRelationship.ANCESTOR

        return NodeRelationship.OTHER

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
        
        # Base case 1: This node has the value we're looking for! Return it.
        if self.val == val:
            return self
        
        # Base case 2: This node is a leaf node. This branch of the search is over, return None.
        if self.is_leaf():
            return None
        
        # Recursive case: Search the left or right subtree depending on numeric comparison
        subtree = self.left if val < self.val else self.right
        return subtree.search(val)

    def __init__(self, val: int, parent: 'TreeNode' = None, depth: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        """Constructs a new instance of `TreeNode`.

        Args:
            val (int): The integer value to store in the tree node.
            parent (TreeNode, optional): Parent of this tree node. Defaults to None.
            depth (int, optional): How deep in the tree this node is. Defaults to 0.
            left (TreeNode, optional): Left child node. Defaults to None.
            right (TreeNode, optional): Right child node. Defaults to None.
        """
        self.val = val
        self.depth = depth
        self.left = left
        self.right = right
        self.parent = parent
