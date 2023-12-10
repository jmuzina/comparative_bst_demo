from entities.Dialogue.DialogueNode import DialogueNode
from typing import List, Callable, Generic, TypeVar
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
        
    
    def validate_input(self, user_input: str) -> bool:        
        if not super().validate_input(user_input):
            return False
        
        for token_as_int in [safe_str_to_int(token) for token in user_input.split(" ")]:
            if token_as_int < 1 or token_as_int > len(self.options):
                print(f"Invalid input: \"{token_as_int}\" is not a valid option.\nAccepting input from {1}-{len(self.options)}, or {self.exit_cmd}.")
                return False
                
        return True
    
    def display_options(self):
        for i in range(len(self.options)):
            print(f"{i+1}:\t{self.options[i].title}")
        
    def prompt_for_input(self) -> str:
        super().prompt_for_input()
        self.display_options()
        return input(f"Select an option ({1}-{len(self.options)}) Or enter \"{self.exit_cmd}\" to exit: ")

    def activate_child(self, child: 'DialogueNode'):
        if child is None:
            raise ValueError(f"Attempted to activate 'None' child of {str(self)}")
        
        self.exit()
        child.input_loop()
    
    def input_loop(self) -> str:
        user_input = super().input_loop()
        matching_option = self.options[safe_str_to_int(user_input) - 1]
        self.activate_child(matching_option)