(function (jQuery) {
  "use strict";
if (jQuery('.d-slider2').length > 0) {
  const options = {
      centeredSlides: false,
      loop: false,
      slidesPerView: 7,
      autoplay:false,
      spaceBetween: 40,
      breakpoints: {
        320: { slidesPerView: 2 },
        550: { slidesPerView: 3 },
        991: { slidesPerView: 4 },
        1400: { slidesPerView: 5 },
        1500: { slidesPerView: 6 },
        1920: { slidesPerView: 7 },
        2040: { slidesPerView: 7 },
        2440: { slidesPerView: 8 }
    },
      pagination: {
          el: '.swiper-pagination'
      },
      // And if we need scrollbar
      scrollbar: {
          el: '.swiper-scrollbar'  
      }
  } 
  new Swiper('.d-slider2',options);
}

if (jQuery('.d-slider3').length > 0) {
  const options = {
      centeredSlides: false,
      loop: true,
      slidesPerView: 6,
      autoplay:false,
      spaceBetween: 32,
      grid: {
        rows: 2,
      },
      breakpoints: {
        320: { slidesPerView: 1 },
        550: { slidesPerView: 2 },
        991: { slidesPerView: 2 },
        1400: { slidesPerView: 3 },
        1500: { slidesPerView: 3},
        1920: { slidesPerView: 3 },
        2040: { slidesPerView: 3 },
        2440: { slidesPerView: 3 }
    },
      pagination: {
          el: '.swiper-pagination'
      },
      // And if we need scrollbar
      scrollbar: {
          el: '.swiper-scrollbar'  
      }
  } 
  new Swiper('.d-slider3',options);
}

})(jQuery)


