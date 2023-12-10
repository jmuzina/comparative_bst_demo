from entities.Dialogue.DialogueNode import DialogueNode
from typing import List
from abc import ABC
from util.str import safe_str_to_int

class IntegerDialogueNode(DialogueNode[List[int]], ABC):
    def __init__(
        self, 
        title: str = '',
        prompt: str = '',
        parent: 'DialogueNode' = None,
        min: int = None,
        max: int = None
    ):
        super().__init__(
            title=title,
            prompt=prompt,
            parent=parent
        ) 
        
        self.min = min
        self.max = max
        
    def transform_input_to_generic_type(self, user_input: str) -> List[int]:
        """Converts user input into a list of integers

        Args:
            user_input (str): Raw user input

        Returns:
            List[int]: `user_input` converted to a list of integers
        """
        
        # discard tokens that are not integers or are empty. Convert the rest to integers
        return [safe_str_to_int(token.strip()) for token in user_input.split(" ") if token is not None and len(token.strip()) > 0]
    
    def validate_input(self, user_input: str) -> bool:
        """Validates user input as a list of integers

        Args:
            user_input (str): User raw input

        Returns:
            bool: Whether the input is valid
        """
        if super().validate_input(user_input):
            return True
        
        # Split the user input into tokens on whitesapce
        tokens: List[str] = [token.strip() for token in user_input.split(" ") if token is not None and len(token.strip()) > 0]
        
        if len(tokens) == 0:
            print("Invalid input: No tokens found.")
            return False
        
        for token in tokens:
            token_as_int = safe_str_to_int(token)
            if token_as_int is None:
                print(f"Invalid input: \"{token}\" is not an integer.")
                return False
            if self.min is not None and token_as_int < self.min:
                print(f"Invalid input: \"{token_as_int}\" is less than {self.min}.")
                return False
            if self.max is not None and token_as_int > self.max:
                print(f"Invalid input: \"{token_as_int}\" is greater than {self.max}.")
                return False
        
        return True

    def get_prompt_text(self) -> str:
        """Extends base class get_prompt_text to include min and max values

        Returns:
            str: Prompt text
        """
        prompt_str = "Enter a space-separated list of integers"
        if self.min is not None or self.max is not None:
            prompt_str += " where each integer is"
            if self.min is not None:
                if self.max is not None:
                    prompt_str += f" between (inclusive) {self.min} and {self.max}"
                else:
                    prompt_str += f" Greater than or equal to {self.min}"
            else:
                prompt_str += f" Less than or equal to {self.max}"
                
            
        prompt_str += f", enter \"{self.exit_cmd}\" to exit"
        
        if self.parent is not None:
            prompt_str += f", or \"{self.back_cmd}\" to go back to {self.parent.title}"
            
        return prompt_str