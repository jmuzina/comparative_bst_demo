# Haskell implementation of BST

## Usage
1.  Install [GHCup](https://www.haskell.org/ghcup/).
1.  Load the program: `ghci src/muzina_bst.hs`
2.  Start main input loop: `main`. From here, you have four options:
    1. Create/Parse BST. Input a space-separated series of integers to create a BST. Duplicates are discarded.
    2. Print BST. Prints out the current BST, if it exists.
    3. Search BST. Input a space-separated series of integerse to search the BST. Nodes with values matching any of the input integers are returned.
    4. Exit. Quits the program.

## Paradigm
The Haskell implementation adopts a functional approach to the BST problem. This causes the program to flow very differently from the Typescript and Python implementations. Instead of being able to count on mutable state and polymorphism to decide control flow, this program makes heavy use of recursion to solve the problem.

For example, the main menu input loop calls itself with `rootNode` or `Nothing` to decide what options will be available in the next input loop. Instead of setting some mutable state in the input_loop, we simply call the loop again with different or identical parameters.

## Key concepts
### Exception handling
In Haskell, there is no way to implicitly catch exceptions. In other languages, mechanisms can be put in place to handle errors occuring in a given segment of code. As with most things in Haskell, calculations that have the possibility of resulting in an error can be implemented by engaging with Haskell's types and monads. 

The programmer must explicitly mark specific expressions that may not return expected results. Haskell compilers then force the programmer to handle the potential for exceptions.

A great example of this is the `TreeNode` data structure in the Haskell implementation.

![Haskell Treenode data structure, showing the `Maybe` declarations](./readme_assets/treenode_datastructure.png)

A BST tree node may not have one or both of its subtrees. This means that the left and right subtrees need to be marked as optional, forcing the handling of the subtrees to be changed elsewhere throughout the program.

![BST search function, showing explicit handling of the `Maybe` subtrees](./readme_assets/treenode_bst_search_maybe_handling.png)

In the figure above, the third argument to `searchBST` is marked as `Maybe TreeNode`, instead of `TreeNode`. This is because, in the course of the BST search algorithm, the `searchBST` function may be called upon a subtree that does not exist, meaning the number is not anywhere in the tree. This needs to be handled gracefully, without error.

The labeled red circles are areas of interest with respect to this concept.
1. The programmer must introduce some branching construct to change how the BST node is handled, based on if it exists (indicated with `Just` monad), or does not (with the `Nothing` monad). `validCurNode` is an alias of `curNode` that can safely be typed as `TreeNode` instead of `Maybe TreeNode`, thus enabling other calculations that depend on the node existing (i.e. getting its numeric value).
2. `searchBST` requires the root of the tree to be passed as an argument to allowed restarting the search from the top of the tree to search for multiple numbers. Thus, `rootNode` is marked `TreeNode`, not `Maybe TreeNode`. In cases where we need to restart from the top of the tree, we pass `rootNode` as `curNode`, but use the `Just` monad to convert it to a `Maybe TreeNode`.

Haskell does share some similarities with the other languages used, in that it allows the programmer to programmatically throw an error with a message. However, Haskell's thrown errors cannot be caught and handled like Typescript and Python's can; Haskell's errors exit the progrma.

### Compiler/Interpreter Optimizations
Haskell compilers have many more opportunities to perform powerful optimizations on recursive functions than other compilers or interpreters can. The binary search implementation provided can be tail-call-optimized by a compiler, if the compiler recognizes the opportunity and takes it. This is because there is no mutable state held in the recursive calls, and the last operation of each non-terminal recursive call is another recursive call. 

In the specific case of a binary search tree, this optimization may not be especially noticable given the inherent efficiency of the binary search algorithm, though more intense calculations, like depth-first searches, may see very significant performance gains from using Haskell. 

### Parameter passing & evaluation
In Haskell, all values (and all parameters) are immutable. Further, the parameter value are not passed into functions per se; rather, "thunking" is used. Function arguments become unevaluated expressions as parameters, and they are not evaluated until their value is actually needed. 