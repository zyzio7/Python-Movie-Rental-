console.log("main.js")

// Instantiate the Bootstrap carousel
$('.multi-item-carousel').carousel({
  interval: false
});

// for every slide in carousel, copy the next slide's item in the slide.
// Do the same for the next, next item.
$('.multi-item-carousel .item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));
  
  if (next.next().length>0) {
    next.next().children(':first-child').clone().appendTo($(this));
  } else {
  	$(this).siblings(':first').children(':first-child').clone().appendTo($(this));
  }
});

$(document).ready(function() {
    $('#movies-table').DataTable();

    var count = $(".product-rating").attr("rate-value");
    for(var i = 1; i < count; i++) {
        $(".product-rating").append('<i class="fa fa-star gold"></i>');
    }
    for(var i = count; i < 10; i++)
    {
        $(".product-rating").append('<i class="fa fa-star-o"></i>');
    }


    if($('#js-cart-empty').length > 0 && $('#js-cart-empty')[0].value < 1) {
        $('#js-checkout-button').prop('disabled', true);

        // $(document).ready(function(){
        //     $('[data-toggle="popover"]').popover();
        // });
    }

} );

