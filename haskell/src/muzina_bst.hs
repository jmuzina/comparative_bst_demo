-- Import `nub` to remove duplicates from a list
-- Import `sort` to sort a list (least to greatest)
import Data.List (nub, sort)

-- Data structure to hold a tree node
data TreeNode = TreeNode {
    -- The actual integer value of the BST node
    val :: Int,
    -- Left subtree if it exists
    left :: Maybe TreeNode,
    -- Right subtree if it exists
    right :: Maybe TreeNode
} deriving (Show) -- quick way to get a full string representation of the node with the print function

-- Convert a line of space-separated tokens to a list of integers
tokensToInts :: String -> [Int]
tokensToInts inputLine = map read (words inputLine)

-- Construct a BST from a list of integers
-- ASSUMES: the input list is sorted and contains no duplicates
intsToBST :: [Int] -> Maybe TreeNode
-- Empty list of integers results in an empty tree
intsToBST [] = Nothing
intsToBST nodeNumbers =
    let
        -- Find the root node index - assuming the input array is sorted, the root node is the middle element
        rootIndex = div (length nodeNumbers) 2
        -- Use rootIndex to get the middle node
        rootNumber = nodeNumbers !! rootIndex
        -- Split the input array into left and right subtrees
        leftSubTree = take rootIndex nodeNumbers
        rightSubTree = drop (rootIndex + 1) nodeNumbers
        -- Recursively construct the left and right subtrees
        rootNode = TreeNode rootNumber
            (intsToBST leftSubTree)
            (intsToBST rightSubTree)
    in  -- Return the root node
        Just rootNode

-- Search BST for a list of numbers
-- Returns a list of nodes that with values that were in the provided `searchNumbers` array.
searchBST :: [Int] -> TreeNode -> Maybe TreeNode -> [TreeNode] -> [TreeNode]
searchBST [] _ _ acc = acc -- BASE CASE: return accumulator immediately if the `searchNumbers` array is empty (all values have been found)
searchBST searchNumbers rootNode curNode acc =
    case curNode of
        -- The current node exists, decide to go left, right, or add the node to the acc if it matches the search value
        Just validCurNode -> let
            -- Get first value from the list of numbers to search for
            searchValue = head searchNumbers
            -- Get the numeric value of the current node
            nodeValue = val validCurNode
            -- Get the left and right subtrees of the current node
            leftSubTree = left validCurNode
            rightSubTree = right validCurNode

            retVal
                -- Current node's value is the same as what we're looking for.
                    -- Add the current node to the accumulator
                    -- Remove the search value from the list of numbers to search for
                    -- Call the function again with one less number to search for
                    -- Use rootNode as curNode, effectively starting over at the top of the BST
                        -- searchBST expects the curNode argument to be optional, so use Just to coerce it to a `Maybe TreeNode`
              | searchValue == nodeValue = searchBST (tail searchNumbers) rootNode (Just rootNode) (validCurNode : acc)
                -- The current node's value is greater than the search value.
                    -- Switch to left subtree and keep searching
              | searchValue < nodeValue = searchBST searchNumbers rootNode leftSubTree acc
                -- The current node's value is less than the search value.
                    -- Switch to right subtree and keep searching
              | otherwise = searchBST searchNumbers rootNode rightSubTree acc

            in retVal
        -- The current node does not exist, so we've reached the end of the BST
            -- This means that the number at the front of the searchNumbers list was not found anywhere in the BST. It is removed before calling again.
            -- Again, coerce rootNode to `Maybe TreeNode` to match fn signature
        Nothing -> searchBST (tail searchNumbers) rootNode (Just rootNode) acc


-- Main input loop
-- Optionally pass in a BST tree node to enable printing and searching that BST
inputLoop :: Maybe TreeNode -> IO ()
inputLoop rootNode = do
    putStrLn "1. Construct BST from input"

    -- Alter how we display options 2 and 3 based on whether or not we have a BST
    case rootNode of
        Just _ -> do
            putStrLn "2. Print BST"
            putStrLn "3. Search BST"
        _ -> do
            putStrLn "2. Print BST (not available - construct BST first)"
            putStrLn "3. Search BST (not available - construct BST first)"

    putStrLn "4. Exit"

    userInput <- getLine
    case userInput of
        "1" -> do
            putStrLn "Enter a space-separated list of numbers:"
            inputLine <- getLine
            -- Construct BST from user input. Input has duplicates removed and is then sorted.
            let rootNode = intsToBST (sort (nub (tokensToInts inputLine)))
            -- Verify that the tree was constructed.
            case rootNode of
                -- Print the tree and re-open main menu with rootNode still in scope
                Just _ -> do
                    print rootNode
                    inputLoop rootNode
                -- If the tree was not constructed, print an error and re-open main menu with rootNode out of scope
                _ -> do
                    putStrLn "An error occurred while constructing the BST."
                    inputLoop Nothing
        "2" -> do
            case rootNode of
                -- Print the tree and re-open main menu with rootNode still in scope
                Just _ -> do
                    print rootNode
                    inputLoop rootNode
                _ -> do
                    putStrLn "Construct BST first"
                    inputLoop Nothing
        "3" -> do
            case rootNode of
                Just validRootNode -> do
                    putStrLn "Enter a space-separated list of numbers to search for:"
                    -- Read user input
                    inputLine <- getLine
                    -- Map user input to list of numbers
                    let searchNumbers = sort (nub (tokensToInts inputLine))
                    -- Perform binary search
                    let nodesMatchingAnySearchedNumbers = searchBST searchNumbers validRootNode (Just validRootNode) []
                    -- Get .val of each node in search result.
                    let searchResultValues = map (show . val) nodesMatchingAnySearchedNumbers
                    -- Convert list of node values to a string
                    let searchResultValuesAsString = unwords (sort searchResultValues)
                    -- Get proportion of values found
                    let proportionFoundString = show (length searchResultValues) ++ "/" ++ show (length searchNumbers)
                    -- Final summary string
                    let summaryString = "Found " ++ proportionFoundString ++ " values:"

                    putStrLn summaryString
                    putStrLn searchResultValuesAsString

                    -- Return to main menu. Pass back `rootNode` so that it it isn't lost
                    inputLoop rootNode
                _ -> do
                    putStrLn "Construct BST first"
                    inputLoop Nothing

        "4" -> putStrLn "Exiting program!"

        _ -> do
            putStrLn "Invalid input"
            inputLoop Nothing

main :: IO ()
main = inputLoop Nothing
