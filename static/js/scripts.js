/*!
* Start Bootstrap - Landing Page v6.0.3 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// 
 $("#id_advance_amount").keyup(function(event) {
    advance_amount = parseFloat($(this).val());
    console.log(advance_amount)
    total_amount = parseFloat($("#id_total_amount").val());
    if( typeof(advance_amount)==="number" &&  typeof(advance_amount) === "number") {
      let pending_amount =  total_amount - advance_amount
      $("#id_pending_amount").val(pending_amount);
      if(pending_amount == 0) {
        $("#id_amount_status").val("completed");
      }else{
        $("#id_amount_status").val("pending");
      }

    }
 });