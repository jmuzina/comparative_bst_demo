import { Component, Input } from '@angular/core';
import { TreeNode } from '../../../entities/TreeNode';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrl: './summary.component.scss'
})
export class SummaryComponent {
  @Input({required: true}) tree?: TreeNode
}
