# Haskell implementation of BST

## Usage
1.  Load the program: `ghci src/muzina_bst.hs`
2.  Start main input loop: `main`. From here, you have four options:
    1. Create/Parse BST. Input a space-separated series of integers to create a BST. Duplicates are discarded.
    2. Print BST. Prints out the current BST, if it exists.
    3. Search BST. Input a space-separated series of integerse to search the BST. Nodes with values matching any of the input integers are returned.
    4. Exit. Quits the program.

## Paradigm
The Haskell implementation adopts a functional approach to the BST problem. This causes the program to flow very differently from the Typescript and Python implementations. Instead of being able to count on mutable state and polymorphism to decide control flow, this program makes heavy use of recursion to solve the problem.

For example, the main menu input loop calls itself with `rootNode` or `Nothing` to decide what options will be available in the next input loop. Instead of setting some mutable state in the input_loop, we simply call the loop again with different or identical parameters.
