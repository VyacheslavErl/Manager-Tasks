$('#workers .arrow-next').click(function(){
    $('#workers .workers-cards').animate({
        scrollLeft: (457 + $('.workers-cards').scrollLeft())
    }, 300);
});

$('#workers .arrow-prev').click(function(){
    $('#workers .workers-cards').animate({
        scrollLeft: ($('.workers-cards').scrollLeft() - 457)
    }, 300);
})

$('.open-popup').on("click", function(){
    $('.popup-bg#' + $(this).attr('id') + 'a').fadeIn(200)
})

$('.close-popup').click(function(event) {
    $(String(event.target.id) +'.popup-bg').fadeOut(200)
})
