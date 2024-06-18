<?php
header("Content-Type:text/css");
$color = "#f0f"; // Change your Color Here
$secondColor = "#ff8"; // Change your Color Here

function checkhexcolor($color){
    return preg_match('/^#[a-f0-9]{6}$/i', $color);
}

if (isset($_GET['color']) AND $_GET['color'] != '') {
    $color = "#" . $_GET['color'];
}

if (!$color OR !checkhexcolor($color)) {
    $color = "#336699";
}


function checkhexcolor2($secondColor){
    return preg_match('/^#[a-f0-9]{6}$/i', $secondColor);
}

if (isset($_GET['secondColor']) AND $_GET['secondColor'] != '') {
    $secondColor = "#" . $_GET['secondColor'];
}

if (!$secondColor OR !checkhexcolor2($secondColor)) {
    $secondColor = "#336699";
}
?>

.counter__item:hover .icon, .footer-wrapper .footer-widget .links li a:hover, .menu li a.active, .section__cate, .faq__item.open .faq__title .title, .text--base, .user__item .user__content .amount, .client__item blockquote::after, .post__item .post__content .meta__date .meta__item i, .post__item .post__read, .footer-wrapper .footer-widget .links li a::before, .contact__item .contact__body a, .contact__item .contact__icon, a , .dashboard-item:hover .dashboard-icon, .widget__post .widget__post__content span, .page-link{
    color: <?php echo $color; ?>;
}

.form-control:focus{
    border-color: <?php echo $color; ?>fe;
}

.post__share li a i, *::selection, .header-top, .header-wrapper .right-area .cmn--btn, .cmn--btn, .feature-item .subtitle::before, .custom-tab-menu .tab-menu li.active .service-icon span, .section__cate::before, .section__cate::after, .faq__item.open .faq__title .right--icon::before, .footer-wrapper .footer-widget .title::after, .scrollToTop, button.cmn--btn:hover, .contact__item:hover .contact__icon, .account__section-wrapper .account__section-content .section__header .section__title::after, .dashboard-item .dashboard-icon, .dashboard-item:hover, .cmn--table thead th, .custom--card button.form--control, .widget__ticket-title::after{
    background: <?php echo $color; ?>;
}

.header-section.active .header-bottom, .footer-middle, .preloader{
    background: <?php echo $secondColor; ?>;
}

.feature-item .subtitle::before{
    -webkit-animation: <?php echo $color; ?>; infinite;
}

.custom-tab-menu::after{
    border: 2px dashed <?php echo $color; ?>;
}

.custom-tab-menu .tab-menu li .service-icon{
    border: 1px solid <?php echo $color; ?>66;
}

.how__thumb{
    color: <?php echo $color; ?>;
    border-color: <?php echo $color; ?>;
}

.post__item .post__content .meta__date{
    border-left: 5px solid <?php echo $color; ?>;
}

h1 a:hover, h2 a:hover, h3 a:hover, h4 a:hover, h5 a:hover, h6 a:hover , .feature-item .icon{
    color: <?php echo $color; ?>;
}

#preloader:before{
    border: 1px solid <?php echo $color; ?>;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 <?php echo $color; ?>85, 0 0 0 0 <?php echo $color; ?>85;
    }

    40% {
        box-shadow: 0 0 0 20px <?php echo $color; ?>00, <?php echo $color; ?>85;
    }

    80% {
        box-shadow: 0 0 0 20px <?php echo $color; ?>00, 0 0 0 20px <?php echo $color; ?>00;
    }

    100% {
        box-shadow: 0 0 0 0 <?php echo $color; ?>00, 0 0 0 0 <?php echo $color; ?>00;
    }
}
.user__item .user__thumb,
.dashboard-menu ul li a:hover, .dashboard-menu ul li a.active{
    border-color: <?php echo $color; ?>;
}

.form--control-2:focus {
    border-color: <?php echo $color; ?>;
}

.btn--primary, .badge--primary, .bg--primary{
    background: <?php echo $color; ?>;
}

.page-item.active .page-link {
    background-color: <?php echo $color; ?>;
    border-color: <?php echo $color; ?>;
}

.page-link:hover, .see-more-less::after, .see-more-less.active span::after{
    color: <?php echo $color; ?>;
}