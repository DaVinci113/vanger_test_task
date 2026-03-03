/* global $ */

$(function () {
  var $main = $(".slider-for");
  var $thumbs = $(".slider-nav");
  var $fullscreen = $(".fullscreen-slider");

  if ($main.length) {
    $main.slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
      asNavFor: ".slider-nav",
      adaptiveHeight: true,
    });
  }

  if ($thumbs.length) {
    $thumbs.slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      asNavFor: ".slider-for",
      dots: false,
      centerMode: false,
      focusOnSelect: true,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 4,
          },
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 3,
          },
        },
      ],
    });
  }

  if ($fullscreen.length) {
    $fullscreen.slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      dots: true,
      adaptiveHeight: true,
    });
  }

  // Open fullscreen gallery on click
  $(document).on("click", ".slider-main-image", function () {
    var index = $(this).data("index") || 0;
    $fullscreen.slick("slickGoTo", index, true);
    var modalEl = document.getElementById("imageModal");
    if (modalEl) {
      var modal = new bootstrap.Modal(modalEl);
      modal.show();
    }
  });
});

