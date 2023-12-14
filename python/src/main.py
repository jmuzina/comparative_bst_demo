from entities.Dialogue.Nodes.RootDialogueNode import RootDialogueNode
    
def main():
    # Program lives as long as the root dialogue input loop continues.
    root_dialogue = RootDialogueNode()
    root_dialogue.input_loop()
    
if __name__ == "__main__":
    main()