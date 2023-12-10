import { Component, Input, OnChanges, OnDestroy, SimpleChanges } from '@angular/core';
import { TreeNode } from '../../../entities/TreeNode';
import { TreeNode as PrimeTreeNode } from 'primeng/api';
import { ITreeSearchEvent } from '../../../entities/Search';

@Component({
  selector: 'jm-display',
  templateUrl: './display.component.html',
  styleUrl: './display.component.scss'
})
export class DisplayComponent implements OnDestroy, OnChanges {
  @Input({required: true}) tree?: TreeNode

  lastSearchEvent?: ITreeSearchEvent;

  /** Use a getter to coerce the prime node into a guaranteed-truthy array, otherwise typescript gets upset */
  get data(): PrimeTreeNode[] {
    return this.tree?.primeNode ? [this.tree.primeNode] : [];
  }

  /**
   * Handle search events from the child search component
   * @param event Search result fired by the child search component
   */
  onSearch(event?: ITreeSearchEvent) : void {
    // Wipe current DOM node highlight
    this.removeHighlight();

    // Apply highlight to the foound DOM node if it exists
    if (event?.node?.domNode) this.applyHighlight(event.node.domNode)

    this.lastSearchEvent = event;
  }

  /**
   * Remove the highlight from the last search result
   */
  private removeHighlight(): void {
    if (this.lastSearchEvent?.node?.domNode) {
      this.lastSearchEvent.node?.domNode.classList.remove('highlighted');
    }
  }

  /**
   * Apply search highlight to a DOM node
   * @param node node to highlight
   */
  private applyHighlight(node: HTMLDivElement) {
    node.classList.add('highlighted');
  }

  ngOnDestroy(): void {
    // Remove the highlight when the component is destroyed
    this.removeHighlight();
  }

  ngOnChanges(changes: SimpleChanges): void {
    // Remove highlight on tree change
    if (changes['tree']) this.removeHighlight();  
  }
}
