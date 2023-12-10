import { Component } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { environment } from '../../environments/environment';

@Component({
  selector: 'jm-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  items: MenuItem[] = [
    {
      label: environment.name,
      url: `/`,
      icon: 'pi pi-home',
    },
    {
      label: 'Julie Muzina',
      url: 'https://jmuzina.io',
      icon: 'pi pi-info-circle',
    },
    {
      icon: 'pi pi-github',
      tooltip: 'GitHub Repository',
      label: 'GitHub',
      url: `${environment.githubRepository.url}/tree/main/typescript`
    }
  ]
}
