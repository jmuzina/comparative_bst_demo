from entities.Dialogue.DialogueNode import DialogueNode
from typing import List
from util.str import safe_str_to_int

class OptionsDialogueNode(DialogueNode[DialogueNode]):    
    def __init__(
        self, 
        prompt: str = '', 
        title: str = '',
        options: List['DialogueNode'] = [], 
        parent: 'DialogueNode' = None,
    ):
        super().__init__(
            title=title,
            prompt=prompt, 
            options=options,
            parent=parent, 
        )
        assert len(self.options) > 0, f"DialogueNode {str(self)} must have at least one option."
        
    def visible_options(self) -> List['DialogueNode']:
        """Get the list of options that should be visible to the user
        This is used to conditionally display a set of dialoge nodes based on the state of the program

        Returns:
            List(DialogueNode): List of dialogue nodes that should be visible
        """
        return self.options
    
    def validate_input(self, user_input: str) -> bool:   
        """Extends base class validate_input to validate that the user's input is a valid option"""  
        
        if super().validate_input(user_input):
            return True
        
        visible_options = self.visible_options()
        
        try: 
            for token_as_int in [safe_str_to_int(token) for token in user_input.split(" ") if token is not None]:
                if token_as_int < 1 or token_as_int > len(visible_options):
                    print(f"Invalid input: \"{token_as_int}\" is not a valid option.\nAccepting input from {1}-{len(visible_options)}, or {self.exit_cmd}.")
                    return False
        except TypeError:
            return False
                
        return True
    
    def get_visible_options(self) -> List['DialogueNode']:
        """Displays all of the available options to the user

        Returns:
            List(DialogueNode): All of the valid options
        """
        visible_options = self.visible_options()
        
        # Only display the options if there is more than one. Otherwise, the user has no choice.
        if (len(visible_options) > 1):
            for i in range(len(visible_options)):
                print(f"{i+1}:\t{visible_options[i].title}")
            
        return visible_options
    
    def get_prompt_text(self) -> str:
        """Extend base prompt text implementation by displaying all of the valid options to the user

        Returns:
            str: Prompt text
        """
        displayed_options = self.get_visible_options()
        
        # Only one option available, auto-select it to save the user a keystroke
        if len(displayed_options) == 1:
            self.activate_child(displayed_options[0])
            return
        
        prompt_str = f"Select an option ({1}-{len(displayed_options)}), enter \"{self.exit_cmd}\" to exit"
        if self.parent is not None:
            prompt_str += f", or \"{self.back_cmd}\" to go back to {self.parent.title}"
        
        return prompt_str

    def activate_child(self, child: 'DialogueNode'):
        """Activates the child node, deactivates the current node, and starts the child's input loop

        Args:
            child (DialogueNode): Node to select

        Raises:
            ValueError: If the child is None
        """
        if child is None:
            raise ValueError(f"Attempted to activate 'None' child of {str(self)}")
        
        self.exit()
        child.input_loop()
        
    def transform_input_to_generic_type(self, user_input: str) -> DialogueNode:
        """Converts user input into a dialogue node with the matching option number

        Args:
            user_input (str): User's raw input - matches the option number for one of `visible_options`

        Returns:
            DialogueNode: _description_
        """
        return self.visible_options()[safe_str_to_int(user_input) - 1]
    
    def on_input_received(self, selected_node: DialogueNode):
        """Activate the dialogue node referenced by the user's input

        Args:
            selected_node (DialogueNode): Node to activate
        """
        self.activate_child(selected_node)