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

## Key concepts
### Exception handling
Python offers block-level exception handling, like Typescript and in contrast to Haskell. Programmers can also mark values as optional, but these markings (referred to in Python as "type hints"), are not actually enforced by the Python interpreter. They are more useful for documentation & readability purposes. So, Python offers much less specific exception handling when it comes to expressing potentially failing computations.

### Compiler/Interpreter Optimizations
Python is an interpreted language, and as such introduces a slightly higher overhead at runtime. Python does not perform significant code optimizations that might be performed by compilers. In this project's case, Python cannot perform tail-call optimization. This does not need to very noticeable performance effects for this use-case, but in more intense workloads, programs written in Rust, Haskell, C, etc. may perform much better. 

### Parameter passing & evaluation
In Python, parameters are passed by object-reference. At function call, a reference to the object containing the actual parameters is passed into the formal parameter. What happens to this reference inside the function depends on whether or not it is mutable. 

- Imutable object references: Types like `int`, `str`, `bool`, etc. have immutable object references when passed as parameters. While the object reference in the formal parameter is initially exactly the same as the actual parameter, when a change is made to the formal parameter a new object reference is created to avoid changing the value of the actual parameters.
- Mutable object references: More complex types, like `dict`, `list`, and instances of user-created datastructures have mutable object references when passed as parameters. Changes to the formal parameter's value also occur to the actual parameter. 

Parameter evaluation is done before calling the function. Expressions must be evaluated before function call time so that their value can be bound to an object reference, even if the value of the parameter is never actually used in the called function.