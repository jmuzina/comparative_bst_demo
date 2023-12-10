from entities.Dialogue.OptionsDialogueNode import OptionsDialogueNode
from entities.Dialogue.DialogueNode import DialogueNode
from entities.BinarySearchTree.TreeNode import TreeNode
from typing import List
from entities.Dialogue.Nodes.ParseBSTDialogueNode import ParseBSTDialogueNode
from entities.Dialogue.Nodes.SearchBSTDialogueNode import SearchBSTDialogueNode

class RootDialogueNode(OptionsDialogueNode[TreeNode]):    
    tree: 'TreeNode' = None
    SearchBSTDialogueNode: 'SearchBSTDialogueNode' = None
    
    def __init__(
        self
    ):
        super().__init__(
            title='Home',
            prompt='Please select a BST operation:',
            options=[
                ParseBSTDialogueNode(parent=self)
            ],
            parent=None, 
        )
        
    def visible_options(self) -> List['DialogueNode']:
        retVal = super().visible_options().copy()
        
        if self.tree is not None:
            retVal.append(self.SearchBSTDialogueNode)
            
        return retVal
    
    def prompt_for_input(self) -> str:
        # Print the current BST if it exists
        if (self.tree is not None):
            print(f"Current BST:\n")
            self.tree.print_report()
            print("\n")
            
        return super().prompt_for_input()
        
    def on_tree_parsed(self, child: DialogueNode, parsed_tree: TreeNode):
        self.tree = parsed_tree if parsed_tree is not None else self.tree
        self.SearchBSTDialogueNode = SearchBSTDialogueNode(
            parent=self, 
            tree=self.tree
        )
        print("Tree parsed successfully.")
        self.tree.print_report()
        
    def on_tree_searched(self, child: DialogueNode, values_searched: List[int], nodes_found: List[TreeNode], values_not_found: List[int]):
        pass