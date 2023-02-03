$(document).ready(function () {
   $('.profilefrm').submit(function (e) { 
    e.preventDefault();
  
      $.ajax({
        type: "post",
        url: "/account/update-profile/",
        data: $(this).serialize(),
        dataType: "text",
        success: function (response) {
         if(response){
            swal({
              title: "Update Suceessfull",
              text: response,
              icon: "success",
              button: "Ok",
            });
         }
        }
      });
       
       
   }); 
    
})