import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'toString' }) 
export class ToStringPipe implements PipeTransform {
    /**
     * Convert any template value input to a string
     * @param input object to call toString() on
     * @returns `input` as a string
     */
    transform(input: any): string {
        return input?.toString();
    } 
}