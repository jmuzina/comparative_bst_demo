from entities.Dialogue.DialogueNode import DialogueNode
from typing import List
from abc import ABC

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
        return [int(token) for token in user_input.split(" ")]
        
    def prompt_for_input(self) -> str:
        super().prompt_for_input()
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
            
            
        prompt_str += f" or enter \"{self.exit_cmd}\" to exit: "
        
        return input(prompt_str)