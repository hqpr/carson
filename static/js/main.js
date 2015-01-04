$(document).ready(function(){
    $('.top-banner-wrapper ul li').css('width', $(window).width() + 'px');

    $(window).resize(function () {
        $('.top-banner-wrapper ul li').css('width', $(window).width() + 'px');
    })
});