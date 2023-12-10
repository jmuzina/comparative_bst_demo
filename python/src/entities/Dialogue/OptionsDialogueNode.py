from entities.Dialogue.DialogueNode import DialogueNode
from typing import List, Generic, TypeVar
from util.str import safe_str_to_int

T = TypeVar('T')

class OptionsDialogueNode(DialogueNode, Generic[T]):    
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
        return self.options
    
    def validate_input(self, user_input: str) -> bool:     
        if user_input == self.exit_cmd:
            return True
           
        if not super().validate_input(user_input):
            return False
        
        visible_options = self.visible_options()
        
        for token_as_int in [safe_str_to_int(token) for token in user_input.split(" ")]:
            if token_as_int < 1 or token_as_int > len(visible_options):
                print(f"Invalid input: \"{token_as_int}\" is not a valid option.\nAccepting input from {1}-{len(visible_options)}, or {self.exit_cmd}.")
                return False
                
        return True
    
    def display_options(self) -> List['DialogueNode']:
        visible_options = self.visible_options()
        
        if (len(visible_options) > 1):
            for i in range(len(visible_options)):
                print(f"{i+1}:\t{visible_options[i].title}")
            
        return visible_options
    
    def get_prompt_text(self) -> str:
        displayed_options = self.display_options()
        
        # Only one option available, auto-select it to save the user a keystroke
        if len(displayed_options) == 1:
            self.activate_child(displayed_options[0])
            return
        
        prompt_str = f"Select an option ({1}-{len(displayed_options)}), enter \"{self.exit_cmd}\" to exit"
        if self.parent is not None:
            prompt_str += f", or \"{self.back_cmd}\" to go back to {self.parent.title}"
        
        return prompt_str

    def activate_child(self, child: 'DialogueNode'):
        if child is None:
            raise ValueError(f"Attempted to activate 'None' child of {str(self)}")
        
        self.exit()
        child.input_loop()
    
    def input_loop(self) -> str:
        user_input = super().input_loop()
        matching_option = self.visible_options()[safe_str_to_int(user_input) - 1]
        self.activate_child(matching_option)