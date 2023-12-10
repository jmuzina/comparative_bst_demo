import { TreeNode } from "./TreeNode";

/**
 * Event emitted when a search is performed on the tree
 */
export interface ITreeSearchEvent {
    searchValue: number
    node?: {
        data: TreeNode,
        domNode: HTMLDivElement
    }
}