from entities.Dialogue.IntegerDialogueNode import IntegerDialogueNode
from typing import List
from entities.BinarySearchTree.TreeNode import TreeNode
from entities.Dialogue.DialogueNode import DialogueNode

class SearchBSTDialogueNode(IntegerDialogueNode):
    tree: TreeNode = None
    
    def __init__(
        self, 
        parent: DialogueNode = None,
        tree: TreeNode = None
    ):
        super().__init__(
            title='Search BST',
            prompt='Input a series of integers to search the BST for, separated by spaces.', 
            parent=parent
        )
        self.tree = tree
        assert self.tree is not None, f"SearchBSTDialogueNode {str(self)} must have a tree to search."
    
    def on_input_received(self, user_input: List[int]):
        """Search the BST for the values in `user_input`

        Args:
            user_input (List[int]): List of integers to search through
        """
        assert self.parent is not None, f"SearchBSTDialogueNode {str(self)} must have a parent."
        
        user_input_unique = sorted(set(user_input))
        vals_not_found: List[int] = []
        nodes_found: List[TreeNode] = []
        
        for node_val in user_input_unique:
            found = self.tree.search(node_val)
            if found is not None:
                nodes_found.append(found)
            else:
                vals_not_found.append(node_val)
                
        # Notify the parent that the search has completed, and pass control back to parent node.
        self.parent.on_tree_searched(
            child=self,
            values_searched=user_input_unique,
            nodes_found=nodes_found,
            values_not_found=vals_not_found
        )
        self.go_back()