import {Component} from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';

/**
 * @title Multi-row toolbar
 */
@Component({
  selector: 'toolbar-multirow.component',
  templateUrl: './toolbar-multirow.component.html',
  styleUrl: './toolbar-multirow.component.css',
  standalone: true,
  imports: [MatToolbarModule, MatIconModule],
})
export class ToolbarMultirowExample {}
