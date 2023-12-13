# Python implementation of BST

## Usage
Make sure that you have Python3 installed first. Then, execute `python3 src/main.py` to start the program. This starts the main input loop.

1. Create/Parse BST: Input a space-separated series of integers to create a BST. Duplicates are discarded.
2. Search BST: Input a space-separated series of integerse to search the BST. Nodes with values matching any of the input integers are returned.

You can also enter `exit` to exit the program, or `back` to go up one level in the menu structure.

## Paradigm
The Python implementation makes use of the following paradigms:
- Object-oriented:
    - Heavy usage of polymorphism for the menu/dialogue system
    - TreeNode class encapsulates the BST node data and methods
- Generic:
    - The `DialogueNode` class is generic. Callers pass in the type that user inputs shall be transformed into.
    - Note that because this is Python and it's not really type-safe, this is moreso an aid for code auto-complete/type hints than it is an actual type safety mechanism.
- Imperative: Within functions, control flow proceeds in an imperative fashion.
- Procedural: Utility function `safe_str_to_int` is heavily used by user input procedures, but is not part of any class.
