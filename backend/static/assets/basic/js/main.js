(function ($) {
  "user strict";

  $('input').prop('autocomplete', true);

  $('input').attr('autocomplete', 'off');

  // Preloader Js
  $(window).on('load', function () {
    $('.preloader').fadeOut(1000);
    var img = $('.bg_img');
    img.css('background-image', function () {
      var bg = ('url(' + $(this).data('background') + ')');
      return bg;
    });
  });
  $(document).ready(function () {
    //Menu Dropdown Icon Adding
    $("ul>li>.submenu").parent("li").addClass("menu-item-has-children");
    // drop down menu width overflow problem fix
    $('ul').parent('li').hover(function () {
      var menu = $(this).find("ul");
      var menupos = $(menu).offset();
      if (menupos.left + menu.width() > $(window).width()) {
        var newpos = -$(menu).width();
        menu.css({
          left: newpos
        });
      }
    });
    $('.menu li a').on('click', function (e) {
      var element = $(this).parent('li');
      if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('li').removeClass('open');
        element.find('ul').slideUp(300, "swing");
      } else {
        element.addClass('open');
        element.children('ul').slideDown(300, "swing");
        element.siblings('li').children('ul').slideUp(300, "swing");
        element.siblings('li').removeClass('open');
        element.siblings('li').find('li').removeClass('open');
        element.siblings('li').find('ul').slideUp(300, "swing");
      }
    })
    $('.select-bar').niceSelect();
    // Scroll To Top 
    var scrollTop = $(".scrollToTop");
    $(window).on('scroll', function () {
      if ($(this).scrollTop() < 500) {
        scrollTop.removeClass("active");
      } else {
        scrollTop.addClass("active");
      }
    });
    $('.client-slider').owlCarousel({
      loop: true,
      nav: false,
      dots: true,
      items: 1,
      autoplay: true,
      margin: 30,
    })
    //header
    var header = $("header");
    $(window).on('scroll', function () {
      if ($(this).scrollTop() < 1) {
        header.removeClass("active");
        $('header, .dashboard-page-header').removeClass('active');
      } else {
        header.addClass("active");
        $('header, .dashboard-page-header').addClass('active');
      }
    });
    //Click event to scroll to top
    $('.scrollToTop').on('click', function () {
      $('html, body').animate({
        scrollTop: 0
      }, 500);
      return false;
    });
    //Header Bar
    $('.header-bar').on('click', function () {
      $(this).toggleClass('active');
      $('.overlay').toggleClass('active');
      $('.menu').toggleClass('active');
      if($('.menu').hasClass('active')) {
        $('.header-wrapper').css('position', 'initial')
      } else {
        $('.header-wrapper').css('position', 'relative')
      }
    })
    $('.overlay').on('click', function () {
      $('.side-menu-area, .menu, .overlay, .header-bar, .dashboard-menu').removeClass('active');
      $('.header-wrapper').css('position', 'relative')
    });
    $('.faq__wrapper .faq__title').on('click', function (e) {
      var element = $(this).parent('.faq__item');
      if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('.faq__content').removeClass('open');
        element.find('.faq__content').slideUp(200, "swing");
      } else {
        element.addClass('open');
        element.children('.faq__content').slideDown(200, "swing");
        element.siblings('.faq__item').children('.faq__content').slideUp(200, "swing");
        element.siblings('.faq__item').removeClass('open');
        element.siblings('.faq__item').find('.faq__title').removeClass('open');
        element.siblings('.faq__item').find('.faq__content').slideUp(200, "swing");
      }
    });
    $('.popup').magnificPopup({
      disableOn: 700,
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false,
      disableOn: 300
    });
    $("body").each(function () {
      $(this).find(".img-pop").magnificPopup({
        type: "image",
        gallery: {
          enabled: true
        }
      });
    });
    $('.custom-tab ul.tab-menu li').on('mouseover', function (g) {
      var tab = $(this).closest('.custom-tab'),
        index = $(this).closest('li').index();
        tab.find('li').siblings('li').removeClass('active');
      $(this).closest('li').addClass('active');
      tab.find('.tab-area').find('div.tab-item').not('div.tab-item:eq(' + index + ')').hide();
      tab.find('.tab-area').find('div.tab-item:eq(' + index + ')').show();
      g.preventDefault();
    });
    $('.header-search-bar').on('click', function() {
      if($(this).hasClass('active')) {
        $(this).removeClass('active')
        $(this).html('<i class="las la-search"></i>')
        $('.header-search-form').hide(300)
      } else {
        $(this).addClass('active')
        $(this).html('<i class="las la-times"></i>')
        $('.header-search-form').show(300)
      }
    })
    $('.dashboard-menu-open').on('click', function() {
        $('.dashboard-menu, .overlay').addClass('active')
    })
    $('.side-sidebar-close-btn').on('click', function() {
        $('.dashboard-menu, .overlay').removeClass('active')
    })
    $('.sponsor-slider').owlCarousel({
      loop: true,
      nav: false,
      dots: false,
      items: 2,
      autoplay: true,
      margin: 20,
      responsive: {
        400: {
          items: 3
        },
        767: {
          items: 4
        },
        992: {
          items: 5
        },
        1200: {
          items: 6
        }
      }
    })
  });
})(jQuery);