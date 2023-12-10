from entities.Dialogue.IntegerDialogueNode import IntegerDialogueNode
from entities.BinarySearchTree.TreeNode import TreeNode
from entities.Dialogue.DialogueNode import DialogueNode
from typing import List

class ParseBSTDialogueNode(IntegerDialogueNode):
    def __init__(
        self, 
        parent: DialogueNode = None,
    ):
        super().__init__(
            title='Parse BST',
            prompt='Input a BST as a list of integers, separated by spaces.', 
            parent=parent
        )
    
    def transform_input_to_generic_type(self, user_input: str) -> TreeNode:
        """Converts node values into a BST

        Args:
            user_input (List[int]): List of integers to convert into a BST

        Returns:
            TreeNode: TreeNode representing the BST root
        """
        user_input_as_ints: List[int] = super().transform_input_to_generic_type(user_input)
        user_input_unique_sorted: List[int] = sorted(set(user_input_as_ints))
        
        return TreeNode.construct_node_from_list(user_input_unique_sorted)
    
    def on_input_received(self, tree: TreeNode):
        """Validate the BST and pass it to the parent node

        Args:
            tree (TreeNode): BST to pass to the parent node
        """
        assert self.parent is not None, f"ParseBSTDialogueNode {str(self)} must have a parent."
        assert tree is not None, f"ParseBSTDialogueNode {str(self)} failed to parse BST."
        
        # Notify parent of the pasrsed BST and pass back control to parent node
        self.parent.on_tree_parsed(self, tree)
        self.go_back()