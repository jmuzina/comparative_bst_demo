from typing import List, Generic, TypeVar
from abc import ABC
import sys

# Generic type T is the type that user inputs are transformed into by `transform_input_to_generic_type`
T = TypeVar('T')

class DialogueNode(ABC, Generic[T]):
    title: str = ""
    prompt: str = ""
    parent: 'DialogueNode' = None
    exit_cmd: str = "exit"
    back_cmd: str = "back"
    active: bool = False
    
    def on_input_received(self, user_input: T):
        """Function to call on receiving valid input from the user

        Args:
            user_input (T): Transformed user input
        """
        # do nothing, allow children to override
        pass
    
    def go_back(self):
        """Returns to the parent node"""
        self.exit()
        
        if self.parent is not None:
            # Start the parent's input loop
            self.parent.input_loop()
        else:
            # If there is no parent, exit the program
            sys.exit(0)
    
    def exit(self):
        """Exits the current node"""
        self.active = False
        
    def enter(self):
        """Enters the current node"""
        self.active = True
           
    def prompt_for_input(self) -> str:
        """Prompts the user for input, and returns their raw input

        Returns:
            str: User's raw input
        """
        print(f"{self.title}:\t{self.prompt}")
        return input(f"\t{self.get_prompt_text()}: ").strip()
        
    def transform_input_to_generic_type(self, user_input: str) -> T:
        """Transform the user's raw input into a generic type

        Args:
            user_input (str): User's raw input

        Returns:
            T: Conversion of the user's raw input to a generic type
        """
        # child classes extend this functionality to actually transform input to generic type
        return None
    
    def get_prompt_text(self) -> str:
        """Gets the text to display to the user when prompting for input

        Returns:
            str: Value to prompt user for input with
        """
        return "Please make a selection"
            
    def input_loop(self) -> str: 
        """Main input loop for the node. Prompts the user for input, and calls `on_input_received` with the transformed input.

        Returns:
            str: User's raw input
        """
        self.enter()
        
        user_input = self.prompt_for_input()
        
        # Continue prompting the user until they enter valid input
        while not self.validate_input(user_input): 
            user_input = self.prompt_for_input()

        # Handle exit and back commands
        if user_input == self.exit_cmd:
            return sys.exit(0)
        if user_input == self.back_cmd:
            return self.go_back()
                    
        # Transform the user's input into a generic type, and call `on_input_received` with the result
        self.on_input_received(self.transform_input_to_generic_type(user_input))
            
        return user_input
    
    def validate_input(self, user_input: str) -> bool:
        """Validates a user raw input str

        Args:
            user_input (str): Raw value entered by user

        Returns:
            bool: Whether the input is valid
        """
        # At the highest level, all exit and back commands are valid.
        if user_input == self.exit_cmd or user_input == self.back_cmd:
            return True
        
        # Child classes extend this functionality to validate further input.
        
        return False
    
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