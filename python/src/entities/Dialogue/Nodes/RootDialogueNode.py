from entities.Dialogue.OptionsDialogueNode import OptionsDialogueNode
from entities.Dialogue.DialogueNode import DialogueNode
from entities.BinarySearchTree.TreeNode import TreeNode
from typing import List
from entities.Dialogue.Nodes.ParseBSTDialogueNode import ParseBSTDialogueNode
from entities.Dialogue.Nodes.SearchBSTDialogueNode import SearchBSTDialogueNode


class RootDialogueNode(OptionsDialogueNode):    
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
        # Update the current BST and create the SearchBSTDialogueNode
        self.tree = parsed_tree if parsed_tree is not None else self.tree
        self.SearchBSTDialogueNode = SearchBSTDialogueNode(
            parent=self, 
            tree=self.tree
        )
        print("Tree parsed successfully.")
        self.tree.print_report()
        
    def on_tree_searched(self, child: DialogueNode, values_searched: List[int], nodes_found: List[TreeNode], values_not_found: List[int]):
        """Display an output report of the search results

        Args:
            child (DialogueNode): Node that emitted the search event
            values_searched (List[int]): List of all values searched for
            nodes_found (List[TreeNode]): List of all nodes found
            values_not_found (List[int]): List of all values not found
        """
        if len(values_searched) == 0:
            print("No values were searched.")
        else:
            print(f"Searching BST for {len(values_searched)} values: {values_searched}")
            if len(nodes_found) == 0:
                print("\tNo nodes were found.")
            else:
                print(f"\tFound {len(nodes_found)}/{len(values_searched)} nodes:")
                for found_node in nodes_found:
                    print(f"\t\t{found_node.val}")
            
            if len(values_not_found) > 0:
                print(f"\tDid not find {len(values_not_found)}/{len(values_searched)} nodes:")
                for not_found_val in values_not_found:
                    print(f"\t\t{not_found_val}")
                
        print("Search complete.")