document.addEventListener('DOMContentLoaded', () => {
  const scroller = document.querySelector('.image-scroller');
  const leftBtn = document.querySelector('.left-btn');
  const rightBtn = document.querySelector('.right-btn');

  let scrollAmount = 0;
  const scrollStep = 220;

  rightBtn.addEventListener('click', () => {
    scrollAmount += scrollStep;
    scroller.style.transform = `translateX(-${scrollAmount}px)`;
  });

  leftBtn.addEventListener('click', () => {
    scrollAmount -= scrollStep;
    if (scrollAmount < 0) scrollAmount = 0;
    scroller.style.transform = `translateX(-${scrollAmount}px)`;
  });
});
