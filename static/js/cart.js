$(document).ready(function () {
    $(".cartfrm, .increament_btn").submit(function (e) {
      e.preventDefault();
      let id = document.getElementById("product_id");
      const product_id = $(this).find('input[id="product_id"]').val();

      $.ajax({
        type: "post",
        url: `/cart/add/${product_id}`,
        data: $(this).serialize(),
        dataType: "json",
        success: function (response) {
          console.log(response);
         
            location.href = "";
          
        },
      });
    });
 
  
  
     $(" .decreament_btn").submit(function (e) {
       e.preventDefault();
   
       let id = document.getElementById("product_id");
       const product_id = $(this).find('input[id="product_id"]').val();
       console.log($(this).find('input[id="product_id"]')[0]);

       $.ajax({
         type: "post",
         url: `/cart/remove/${product_id}`,
         data: $(this).serialize(),
         dataType: "json",
         success: function (response) {
           console.log(response);

           location.href = "";
         },
       });
     });
     $(" .delete_btn").submit(function (e) {
       e.preventDefault();
   
       let id = document.getElementById("product_id");
       const product_id = $(this).find('input[id="product_id"]').val();
       console.log($(this).find('input[id="product_id"]')[0]);

       $.ajax({
         type: "post",
         url: `/cart/delete/${product_id}`,
         data: $(this).serialize(),
         dataType: "json",
         success: function (response) {
           console.log(response);

           location.href = "";
         },
       });
     });
});