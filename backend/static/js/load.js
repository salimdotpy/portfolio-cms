$(window).ready(function () {
    $(".loading").fadeOut("slow")
});
// ========================================================================================================
//Don't tamper my touchable carousel(Image slider) function
$(function () {
    var carousels = $('.carousel');
    carousels.each(function (i) {
        var element = $(this);
        element.carousel();
        element.find('.left').click(function () {element.carousel('prev')});
        element.find('.right').click(function () {element.carousel('next')});
        element.touchStartX = element.touchEndX = 0;
        element.distance = 100;
        element.handleTS = function (event) {
            if (event.touches && event.touches.length > 0) element.touchStartX = event.touches[0].clientX;
        };
        element.handleTM = function (event) {
            element.touchEndX = 0;
            if (event.touches && event.touches.length > 0) element.touchEndX = event.touches[0].clientX;
        };
        element.handleTE = function (event) {
            var space = element.touchEndX - element.touchStartX;
            console.log(element.touchStartX, element.touchEndX, space);
            if (space > element.distance) element.carousel('prev');
            else if (space < -element.distance) element.carousel('next');
        };
        element.ce = document.getElementsByClassName('carousel')[i];
        element.ce.addEventListener('touchstart', element.handleTS);
        element.ce.addEventListener('touchmove', element.handleTM);
        element.ce.addEventListener('touchend', element.handleTE);
    })
});
// ========================================================================================================

    //My own image slider start here
$(function () {
    var tId = null, container = $('.slider-container');
    container.each(function () {
        var element = $(this);
        element.intval = ($(this).data('my-interval') === undefined) ? 5000 : $(this).data('my-interval');
        element.sld = function (type) {
            type = (type === undefined) ? 'right' : type;
            var allw = element[0].scrollWidth - element[0].clientWidth;
            var d = element.find('.slide:first-child').width(), alls = element.find('.slide');
            alls.each(function (i) {
                $(this).text('/' + alls.length)
            });
            var dir = (type == 'left') ? '-=' + d : '+=' + d;
            if (element[0].scrollLeft == 0 && type == 'left') dir = allw;
            else if (element[0].scrollLeft == allw && type != 'left')dir = 0;
            element.find('.slide').css('scroll-snap-align', 'none');
            element.stop().animate({scrollLeft: dir}, 1000);
            setTimeout(function () {
                element.find('.slide').css('scroll-snap-align', 'center');
            }, 1000);
        };
        element.tId = setInterval(function () {
            element.sld()
        }, element.intval);
        element.hover(function (ev) {
            clearInterval(element.tId);
        }, function () {
            element.tId = setInterval(function (ev) {
                element.sld()
            }, element.intval);
        });
        element.find('span.btn.right').click(function () {
            element.sld('right')
        });
        element.find('span.btn.left').click(function () {
            element.sld('left')
        });
    });
});
//    My own image slider end here
