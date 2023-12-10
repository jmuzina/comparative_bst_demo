from typing import List, Callable#, Generic, TypeVar
from abc import ABC, abstractmethod 

#T = TypeVar('T')
class DialogueNode(ABC):
    prompt: str = ""
    options: List['DialogueNode'] = []
    parent: 'DialogueNode' = None
    exit_cmd: str = "exit"
    active: bool = False
    on_input_callback: Callable[[str], str] = None
    
    def validate_input(self, user_input: str) -> bool:
        tokens: List[str] = user_input.split()
        for token in tokens:
            try:  
                token_as_int = int(token)
                if token_as_int < 1 or token_as_int > len(self.options):
                    print(f"Invalid input: \"{token}\" is not a valid option.\nAccepting input from {1}-{len(self.options)}, or {self.exit_cmd}.")
                    return False
                
            except ValueError:
                print(f"Invalid input: \"{token}\" is not a number.")
                return False
        
        return True
    
    def exit(self):
        if self.parent is None:
            return
        
        self.active = False
        self.parent.input_loop()
    
    def display_options(self):
        print(str(self))
        for i in range(len(self.options)):
            print(f"{i+1}:\t{self.options[i]}")
        
            
    def prompt_for_input(self) -> str:
        self.display_options()
        return input(f"Select an option ({1}-{len(self.options)}) Or enter \"{self.exit_cmd}\" to exit: ")
            
    
    def input_loop(self) -> str: 
        self.active = True
        user_input = self.prompt_for_input()
        
        while not self.validate_input(user_input): 
            user_input = self.prompt_for_input()
            if user_input == self.exit_cmd:
                return self.exit()
            
        if self.on_input_callback is not None:
            self.on_input_callback(user_input)
            
        return user_input
    
    def __init__(
        self, 
        prompt: str = '', 
        options: List['DialogueNode'] = [], 
        parent: 'DialogueNode' = None,
        on_input_callback: Callable[[str], str] = None
    ):
        self.prompt = prompt
        self.options = options
        self.parent = parent
        self.on_input_callback = on_input_callback
        assert len(self.options) > 0, f"DialogueNode {str(self)} must have at least one option."

    def __str__(self):
        return self.prompt