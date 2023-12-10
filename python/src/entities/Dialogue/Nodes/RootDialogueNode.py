from ..DialogueNode import DialogueNode
from typing import List, Callable#, Generic, TypeVar

class RootDialogueNode(DialogueNode):
    def __init__(
        self, 
        options: List['DialogueNode'] = [], 
    ):
        super().__init__(
            prompt='Root node', 
            options=[], 
            parent=None, 
            on_input_callback=self.on_input_callback
        )
        
    def validate_input(self, user_input: str) -> bool:
        return super().validate_input(user_input)
    
    
    def on_input_callback(self, user_input: str):
        print(user_input)