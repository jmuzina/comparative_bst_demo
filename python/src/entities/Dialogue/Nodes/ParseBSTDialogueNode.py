from entities.Dialogue.IntegerDialogueNode import IntegerDialogueNode
from entities.BinarySearchTree.TreeNode import TreeNode
from entities.Dialogue.DialogueNode import DialogueNode

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
        
    def validate_input(self, user_input: str) -> bool:
        return super().validate_input(user_input)
    
    def transform_input_to_generic_type(self, user_input: TreeNode) -> TreeNode:
        # remove duplicates and sorts from least to greatest
        user_input_integers = sorted(set(super().transform_input_to_generic_type(user_input)))
        return TreeNode.construct_node_from_list(user_input_integers)
    
    def on_input_received(self, tree: TreeNode):
        assert self.parent is not None, f"ParseBSTDialogueNode {str(self)} must have a parent."
        assert tree is not None, f"ParseBSTDialogueNode {str(self)} failed to parse BST."
        
        self.parent.on_tree_parsed(self, tree)
        self.go_back()