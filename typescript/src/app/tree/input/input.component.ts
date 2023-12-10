import { Component, Input, EventEmitter, Output, OnInit } from '@angular/core';
import { TreeNode } from '../../../entities/TreeNode';
import { AbstractControl, FormArray, FormBuilder, FormGroup, ValidatorFn, Validators } from '@angular/forms';

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrl: './input.component.scss'
})
export class InputComponent implements OnInit {
  @Input({required: true}) tree?: TreeNode
  @Output() treeChange = new EventEmitter<TreeNode | undefined>();

  @Input() min?: number;
  @Input() max?: number;

  controlsKey = 'node_values';
  inputClass = 'node-value-input';

  form?: FormGroup;

  private getInitialForm(): FormGroup {
    return this._fb.group({
      node_values: this._fb.array([], [Validators.required, Validators.minLength(1)])
    })
  }

  /**
   * @returns Array of validators for the node value input
   */
  private getElementValidators(): ValidatorFn[] {
    const elementValidators = [Validators.required];
    
    if (this.min || this.min === 0) elementValidators.push(Validators.min(this.min));
    if (this.max || this.max === 0) elementValidators.push(Validators.max(this.max));

    return elementValidators;
  }

  /**
   * Adds a new control to the form, then focuses the new control.
   */
  addControl(): void {
    const nodeValues: FormArray = this.form?.get(this.controlsKey) as FormArray;
    const newControl = this._fb.control(null, this.getElementValidators());

    nodeValues.push(newControl);

    this.focusLastControl();
  }

  /**
   * Gets an array of all node value controls, as a form-array
   * This is useful so that we can push/remove from the array per user input
   * @returns Node value control group, as a form-array.
   */
  nodeArray(): FormArray {
    return this.form?.get(this.controlsKey) as FormArray;
  }

  /**
   * Returns form group of all node value controls
   * @returns FormGroup (nested, string key for each populated node control)
   */
  nodeControls() : FormGroup {
    return this.nodeArray() as unknown as FormGroup
  }

  /**
   * Gets the control at the given index.
   * @param index index to find
   * @returns control as an AbstractControl
   */
  getControl(index: number) : AbstractControl {
    return this.nodeControls().get(index.toString()) as AbstractControl
  }

  /**
   * Removes the control at the given index.
   * @param index idnex to remove
   */
  removeControl(index: number): void {
    if (index < 0) return;
    
    const nodeValues: FormArray = this.form?.get(this.controlsKey) as FormArray;

    nodeValues.removeAt(index);
  }

  /**
   * Returns the FormGroup within the form at the given index.
   * This is useful for angular's nested formgroups, so that each row can directly bind to a sub-FormGroup.
   * @param index index to find
   * @returns ArrayControl coerced to a FormGroup.
   */
  getArrayControl(index: number) : FormGroup {
    return this.form?.controls[this.controlsKey].get(index.toString()) as FormGroup;
  }

  /** Get all of the input element DOM nodes */
  get inputElements() : NodeListOf<HTMLInputElement> {
    return document.querySelectorAll(`.${this.inputClass} input`);
  }

  /**
   * Adds a new control to the form and focuses it.
   */
  addAndFocusNewControl() : void {
    this.addControl();
    this.focusLastControl();
  }

  /**
   * Gets the last input control and focuses it.
   */
  focusLastControl(): void {
    // Use a short delay to make sure the DOM has updated
    setTimeout(() => {
      const { inputElements } = this;
      const lastInputElement = inputElements.item(inputElements.length - 1);
      lastInputElement?.focus();
    }, 50);
  }

  onSubmit(): void {
    if (!this.form?.valid) return;

    const nodeValues: FormArray = this.form?.get(this.controlsKey) as FormArray;
    const nodeValuesUniqueSorted = nodeValues.value
      .filter((val: number, index: number, arr: number[]) => arr.indexOf(val) === index)
      .sort((a: number, b: number) => a - b);

    const tree = TreeNode.constructNodeFromList(nodeValuesUniqueSorted);
    if (tree) tree.populatePrimeNode();
    this.treeChange.emit(tree || undefined);
  }

  ngOnInit(): void {
    this.form = this.getInitialForm();
    if (!this.tree) this.addControl();
  }

  constructor(private _fb: FormBuilder) { }
}
