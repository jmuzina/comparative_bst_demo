import sys
from typing import List
from entities.BinarySearchTree.TreeNode import TreeNode

def preprocess_args(raw_args: list[str]) -> List[int]:
    """Validates and pre-processes the arguments provided to the program.
        Aborts the program if:
            - No arguments are provided
            - Any argument is not an integer

    Args:
        raw_args (list[str]): Raw list of strings provided to the program.

    Returns:
        List[int]: Arguments provided to the program, as integers.
    """
    def args_to_integers(raw_args: list[str]) -> List[int]:
        int_args: list[int] = []
        for arg in raw_args:
            try:
                # Coerce the argument to an integer
                arg_as_num = int(arg)
                # If an exception was not thrown, the argument is an integer and can be added to the int_args
                int_args.append(arg_as_num)
            except ValueError:
                # If an exception was thrown, the argument is not an integer and the program should exit
                print(f"Invalid integer argument: {arg} must be an integer.")
                sys.exit(1)

        return int_args

    # Remove duplicates and sort the list of integers
    # List must be sorted to ensure tree is as balanced as possible
    int_args = sorted(
        list(
            set(
                args_to_integers(raw_args)
            )
        )
    )
    
    if (len(int_args) == 0):
        print("No integers provided. Please provide a list of integers.")
        sys.exit(1)

    return int_args
    
def main():
    args = preprocess_args(sys.argv[1:])
    root = TreeNode.construct_node_from_list(args)
    root.print_report()

if __name__ == "__main__":
    main()

#todo: figure out a way to let the user construct a tree from a list of integers, and search it and print the found node.
#some kind of tree dialogue structure is needed for this!