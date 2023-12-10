from ..IntegerDialogueNode import IntegerDialogueNode
from typing import List, Callable#, Generic, TypeVar
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
    
    def print_after_input(self, user_input: TreeNode):
        return user_input.print_report()
    
    def transform_input_to_generic_type(self, user_input: str) -> TreeNode:
        user_input_integers = super().transform_input_to_generic_type(user_input)
        return TreeNode.construct_node_from_list(user_input_integers)