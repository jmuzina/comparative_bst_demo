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
        
    def validate_input(self, user_input: str) -> bool:
        return super().validate_input(user_input)
    
    def on_input_received(self, user_input: List[int]):
        assert self.parent is not None, f"SearchBSTDialogueNode {str(self)} must have a parent."
        
        user_input_unique = set(user_input)
        vals_found: List[int] = []
        vals_not_found: List[int] = []
        nodes_found: List[TreeNode] = []
        
        for node_val in user_input_unique:
            found = self.tree.search(node_val)
            if found is None:
                vals_found.append(node_val)
                nodes_found.append(found)
                print(f"{node_val} not found in BST.")
            else:
                vals_not_found.append(node_val)
                print(f"{node_val} found in BST.")
                
        self.parent.on_tree_searched(self, vals_found, nodes_found, vals_not_found)
        self.go_back()