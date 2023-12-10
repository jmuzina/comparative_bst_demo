from typing import List, Generic, TypeVar
from abc import ABC
import sys

T = TypeVar('T')

class DialogueNode(ABC, Generic[T]):
    title: str = ""
    prompt: str = ""
    parent: 'DialogueNode' = None
    exit_cmd: str = "exit"
    back_cmd: str = "back"
    active: bool = False
    
    def on_input_received(self, user_input: T):
        # do nothing, allow children to override
        pass
    
    def go_back(self):
        self.exit()
        if self.parent is not None:
            self.parent.input_loop()
        else:
            sys.exit(0)
    
    def exit(self):
        self.active = False
    
    def display_options(self):
        print(self.prompt)
        for i in range(len(self.options)):
            print(f"{i+1}:\t{self.options[i].title}")
           
    def prompt_for_input(self) -> str:
        print(f"{self.title}:\t{self.prompt}")
        return input(f"\t{self.get_prompt_text()}: ")
        
    def transform_input_to_generic_type(self, user_input: str) -> T:
        # child classes extend this functionality to actually transform input to generic type
        return None
    
    def get_prompt_text(self) -> str:
        return "Please make a selection"
            
    def input_loop(self) -> str: 
        self.active = True
        user_input = self.prompt_for_input().strip()
        if user_input == self.exit_cmd:
            return sys.exit(0)
        if user_input == self.back_cmd:
            return self.go_back()
        
        while not self.validate_input(user_input): 
            user_input = self.prompt_for_input().strip()
            if user_input == self.exit_cmd:
                return sys.exit(0)
            if user_input == self.back_cmd:
                return self.go_back()
            
        self.on_input_received(self.transform_input_to_generic_type(user_input))
            
        return user_input
    
    def validate_input(self, user_input: str) -> bool:
        return True
    
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