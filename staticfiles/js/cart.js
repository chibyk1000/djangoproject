$(document).ready(function () {
    $('.cartfrm').submit(function (e) { 
        e.preventDefault();
        const product_id = $('.product_id').val()
     $.ajax({
       type: "post",
       url: `/cart/add/${product_id}`,
       data: $(this).serialize(),
       dataType: "json",
         success: function (response) {
           console.log(response)
       },
     });
    });
});