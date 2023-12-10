import { Component, Input } from '@angular/core';
import { TreeNode } from '../../../entities/TreeNode';
import { TreeNode as PrimeTreeNode } from 'primeng/api';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrl: './display.component.scss'
})
export class DisplayComponent {
  @Input({required: true}) tree?: TreeNode

  /** Use a getter to coerce the prime node into a guaranteed-truthy array, otherwise typescript gets upset */
  get data(): PrimeTreeNode[] {
    return this.tree?.primeNode ? [this.tree.primeNode] : [];
  }
}
