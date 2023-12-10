from typing import List, Generic, TypeVar
from abc import ABC, abstractmethod
from util.str import safe_str_to_int

T = TypeVar('T')

class DialogueNode(ABC, Generic[T]):
    title: str = ""
    prompt: str = ""
    parent: 'DialogueNode' = None
    exit_cmd: str = "exit"
    active: bool = False
    
    def validate_input(self, user_input: str) -> bool:
        tokens: List[str] = user_input.split()
        for token in tokens:
            token_as_int = safe_str_to_int(token)
            if token_as_int is None:
                print(f"Invalid input: \"{token}\" is not an integer.")
                return False
        
        return True
    
    def print_after_input(self, user_input: T):
        # do nothing, allow children to override
        pass
    
    def go_back(self):
        self.exit()
        if self.parent is not None:
            self.parent.input_loop()
    
    def exit(self):
        self.active = False
    
    def display_options(self):
        print(self.prompt)
        for i in range(len(self.options)):
            print(f"{i+1}:\t{self.options[i].title}")
           
    def prompt_for_input(self) -> str:
        print(self.prompt)
        
    def transform_input_to_generic_type(self, user_input: str) -> T:
        return None
            
    def input_loop(self) -> str: 
        self.active = True
        user_input = self.prompt_for_input()
        
        while not self.validate_input(user_input): 
            user_input = self.prompt_for_input()
            if user_input == self.exit_cmd:
                return self.go_back()
            
        transformed_val: T = self.transform_input_to_generic_type(user_input)
            
        self.print_after_input(transformed_val)
            
        if self.parent is not None:
            self.parent.receive_input_from_child(self, transformed_val)
            
        return user_input
    
    def receive_input_from_child(self, child: 'DialogueNode', child_output: T):
        # do nothing, allow child to override
        pass
    
    def __init__(
        self, 
        title: str = '',
        prompt: str = '', 
        options: List['DialogueNode'] = [], 
        parent: 'DialogueNode' = None,
    ):
        self.title = title
        self.prompt = prompt
        self.options = options
        self.parent = parent

    def __str__(self):
        return self.prompt