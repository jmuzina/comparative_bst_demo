import { Component, EventEmitter, Input, OnChanges, Output, SimpleChanges } from '@angular/core';
import { TreeNode } from '../../../../entities/TreeNode';
import { ITreeSearchEvent } from '../../../../entities/Search';

@Component({
  selector: 'jm-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent implements OnChanges {
  /** Tree from parent node */
  @Input({ required: true }) tree!: TreeNode;
  /** Event emitter for search events */
  @Output() search = new EventEmitter<ITreeSearchEvent | undefined>();

  /** Currently active search number - whatever the user last submitted*/
  appliedSearchValue?: number;
  /** Live search value - not necessarily the submitted one */
  liveSearchValue?: number;

  /**
   * Perform a search on the tree, and emit the result
   * @param searchVal number the user searched for
   * @returns Search results object
   */
  performSearch(searchVal?: number) : ITreeSearchEvent | undefined {
    // Update the applied search value to the new search value
    this.appliedSearchValue = searchVal;

    let searchResult: ITreeSearchEvent | undefined = undefined;

    if (this.appliedSearchValue || this.appliedSearchValue === 0) {
      const matchingNode = this.tree.search(this.appliedSearchValue);

      // If we found a matching node, get the DOM node and emit the search result
      if (matchingNode) {
        const domNode = matchingNode.getDOMNode();
        if (domNode) {

          searchResult = {
            node: {
              data: matchingNode,
              domNode
            },
            searchValue: this.appliedSearchValue
          };
        }
      }
    }

    // Emit the search result to parent component
    this.search.emit(searchResult);
    return searchResult
  }

  /** Placeholder text for the search input */
  get placeholder(): string {
    return `Search${this.appliedSearchValue || this.appliedSearchValue === 0 ? ' (currently ' + this.appliedSearchValue.toString() + ')' : ''}`;
  }

  /**
   * Reset the state of the search keyword inputs
   * Emits an undefined search event to the parent component
   */
  resetSearch(): void {
    this.appliedSearchValue = undefined;
    this.liveSearchValue = undefined;
    this.search.emit(undefined);
  }

  ngOnChanges(changes: SimpleChanges) {
    // Wipe the search state if the tree changes
    if (changes['tree']) this.resetSearch();
  }

}
