import { Component, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-quisuisje',
  standalone: true,
  templateUrl: './quisuisje.component.html',
  styleUrls: ['./quisuisje.component.scss']
})
export class QuisuisjeComponent implements AfterViewInit {

  ngAfterViewInit() {
    let currentPage = 0;
    const pages = document.querySelectorAll('.page');
    const totalPages = pages.length;

    const updatePages = () => {
      pages.forEach((page, index) => {
        if (index < currentPage) {
          page.setAttribute('style', 'transform: rotateY(-180deg);');
        } else if (index === currentPage) {
          page.setAttribute('style', 'transform: rotateY(0deg);');
        } else {
          page.setAttribute('style', 'transform: rotateY(180deg);');
        }
      });
    };

    document.querySelector('.next')?.addEventListener('click', () => {
      if (currentPage < totalPages - 1) {
        currentPage++;
        updatePages();
      }
    });

    document.querySelector('.prev')?.addEventListener('click', () => {
      if (currentPage > 0) {
        currentPage--;
        updatePages();
      }
    });

    // Initial update
    updatePages();
  }
}
