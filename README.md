# BST Implementation Comparison - Python / Haskell / Typescript

## Features 
This project delivers the following capabilities, in multiple programming languages and paradigms:
- Binary search tree creation
    - User is prompted to input numeric values
    - Input is parsed and used to construct a binary search tree
- Binary search tree search
    - User can search the binary search tree for a value, and view the result.

## Languages
A variety of languages were selected to allow for interesting distinctions between implementations, concepts, and paradigms. 
Each language has its own folder at the root of the project, and has its own `README.md` file explaining the specifics of its implementation and usage.
### Python 🐍
The Python implementation uses a dialogue-based approach to enable the user to create and search binary search trees. An object-oriented approach is used to control data validation and menu control flow.
### Haskell  λ
Similarly to the Python implementation, the Haskell implementation uses a menu-based approach and offers the same capabilities. This program is purely functional, using recursion instead of polymorphism to control how the dialogue progresses. 
### Typescript 🌐
The Typescript implementation is a fun little bonus! Admittedly, I made the Python and Typescript implementations first because I am very comfortable with those languages, and then realized I missed the assignment requirement to use two different paradigms and created the Haskell implementation. The Typescript version also takes advantage of Javascript's integration with web browsers to offer a web interface, available at [bst.jmuzina.io](https://bst.jmuzina.io). 