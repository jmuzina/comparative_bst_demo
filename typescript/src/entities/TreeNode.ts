import { TreeNode as PrimeTreeNode } from 'primeng/api';

export const DEFAULT_PRIME_TREE_NODE: PrimeTreeNode<TreeNode> = {
    label: '',
    data: undefined,
    children: []
}

/**
 * Represents a node in a binary tree.
 */
export class TreeNode {
    /** Node's numeric content */
    val: number;

    parent?: TreeNode;

    /** Left subtree */
    left?: TreeNode;

    /** Right subtree */
    right?: TreeNode;

    /** Depth of the node in the tree. Root has depth of 0. */
    depth!: number;

    /** PrimeNG-compatibile treenode for org-chart style displaying */
    primeNode!: PrimeTreeNode<TreeNode>;

    constructor(nodeNumbers: number[], parent?: TreeNode) {
        if (!nodeNumbers.length) throw new Error("Cannot construct a tree node from an empty list.");

        const rootIndex = Math.floor(nodeNumbers.length / 2);
        const rootNumber = nodeNumbers[rootIndex];

        const leftSubTree = nodeNumbers.slice(0, rootIndex);
        const rightSubTree = nodeNumbers.slice(rootIndex + 1);

        this.val = rootNumber;
        this.parent = parent;
        this.depth = parent ? parent.depth + 1 : 0;
        this.primeNode = DEFAULT_PRIME_TREE_NODE;


        if (leftSubTree.length) this.left = new TreeNode(leftSubTree, this);
        if (rightSubTree.length) this.right = new TreeNode(rightSubTree, this);

        this.populatePrimeNode();
    }

    /**
     * Returns whether two tree nodes are equal.
     * @param a First tree node.
     * @param b Second tree node.
     * @returns Whether these two tree nodes are exactly equal.
     */
    static equals(a: TreeNode | null, b: TreeNode | null): boolean {
        // We can assume that tree nodes are unique, so we can compare them by value
        return a?.val === b?.val;
    }

    /**
     * Returns whether this node is the root of the tree.
     * @returns Whether this node is a tree root (has no parent).
     */
    isRoot(): boolean {
        return !!!this.parent;
    }

    /**
     * Returns whether this node is a leaf node (has no children).
     * @returns Whether this node is a leaf node.
     */
    isLeaf(): boolean {
        return !this.children().length;
    }

    /**
     * Returns a list of the children of this node.
     * @returns All children of this node.
     */
    children(): TreeNode[] {
        const allChildren = [this.left, this.right];
        const truthyChildren: TreeNode[] = allChildren.filter(node => !!node) as TreeNode[];
        return truthyChildren
    }

    /**
     * Returns a list of all ancestors (parent, grandparent, etc.) of this node.
     * @returns All ancestors of this node.
     */
    ancestors(): TreeNode[] {
        if (!this.parent) return [];

        return [this.parent, ...this.parent.ancestors()];
    }

    /**
     * Returns a list of all descendants (children, children's children, etc.) of this node.
     * @returns All descendants of this node.
     */
    descendants(): TreeNode[] {
        return this.children().reduce(
            (acc, child) => [...acc, child, ...child.descendants()], 
            new Array<TreeNode>()
        );
    }

    /**
     * Searches the tree for a node with the given value.
     * @param val Value to search for.
     * @returns Node with `val`=`val`, if found. Else, `null`.
     */
    search(val: number): TreeNode | null {
        if (!this) throw new Error("Cannot search a null tree.");
        
        // Base case 1: This node has the value we're looking for! Return it.
        if (this.val === val) return this;

        // Base case 2: This node is a leaf node. This branch of the search is over, return None.
        if (this.isLeaf()) return null;

        // Decide on left or right subtree based on numeric comparison
        const subtree = val < this.val ? this.left : this.right;
        
        if (!subtree) return null;
        
        // Recursive case: Search the appropriate subtree
        return subtree.search(val);
    }

    populatePrimeNode(): void {
        this.primeNode = this.toPrimeTreeNode() || DEFAULT_PRIME_TREE_NODE;
    }

    /**
     * Converts the tree to a PrimeNG-compatible treenode.
     * @returns PrimeNG org chart tree node
     */
    toPrimeTreeNode(): PrimeTreeNode {
        return {
            label: this.val.toString(),
            data: this,
            expanded: true,
            styleClass: this.getDOMClass(),
            children: this.children().map(child => child.toPrimeTreeNode())
        }
    }

    getDOMClass(): string {
        return `orgchart-item-${this.val.toString()}`   
    }

    getDOMNode(): HTMLDivElement | null {
        const matchingDOMNodes = document.getElementsByClassName(this.getDOMClass());
        if (!matchingDOMNodes?.length) return null;
        return matchingDOMNodes[0] as HTMLDivElement;
    }
}
