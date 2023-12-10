import { Component } from '@angular/core';
import { TreeNode } from '../../entities/TreeNode';

@Component({
  selector: 'jm-tree',
  templateUrl: './tree.component.html',
  styleUrl: './tree.component.scss'
})
export class TreeComponent {
  tree?: TreeNode;
  activeIndex = 0;

  onTreeChange(tree?: TreeNode) {
    this.tree = tree;

    // If a tree was created, switch view to the tree after a short delay to give the tree a chance to be populated
    if (tree) {
      setTimeout(() => {
        this.activeIndex = 1;
      }, 50);
    }
  }
}
