from ..OptionsDialogueNode import OptionsDialogueNode
from ..DialogueNode import DialogueNode
from entities.BinarySearchTree.TreeNode import TreeNode
from typing import List
from entities.Dialogue.Nodes.ParseBSTDialogueNode import ParseBSTDialogueNode

class RootDialogueNode(OptionsDialogueNode[TreeNode]):    
    root: 'TreeNode' = None
    
    def __init__(
        self, 
        options: List['DialogueNode'] = [], 
    ):
        super().__init__(
            prompt='Welcome to Julie\'s BST project. Please select an option:',
            options=[
                ParseBSTDialogueNode(parent=self)
            ],
            parent=None, 
        )
        
    def receive_input_from_child(self, child: DialogueNode, parsed_tree: TreeNode):
        self.tree = parsed_tree