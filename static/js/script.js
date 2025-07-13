$(document).ready( function() {
    let isSubmitting = false;

 $("input[name='pizza']").on("change", function() {

		if ($(this).is(":checked")) {
			$(this).val(1);
		} else {
			$(this).val(0);
		}

	});

	$("input[name='pasta']").on("change", function() {

		if ($(this).is(":checked")) {
			$(this).val(1);
		} else {
			$(this).val(0);
		}

	});

	$("input[name='pap']").on("change", function() {

		if ($(this).is(":checked")) {
			$(this).val(1);
		} else {
			$(this).val(0);
		}

	});

	$("input[name='other']").on("change", function() {

		if ($(this).is(":checked")) {
			$(this).val(1);
		} else {
			$(this).val(0);
		}

	});

	function checkAge(dateStr) {
    	
    	var birthDate = new Date(dateStr);
    
    	var currentDate = new Date();
    
    	var dateDifference = currentDate - birthDate;
    
    	var age = Math.floor(dateDifference / (1000 * 60 * 60 * 24 * 365));
    
    	return age;
   	}

   	$("input[name='date']").on("input", function() {
   		const date = $(this).val();
   		const age = checkAge(date);

   		if (age < 5 || age > 120) {
   			alert("You must be over 5 year old, and younger than 120 years!");
   			location.reload();
   		} else {
   			parseInt($("#date_value").val(age));
   		}


   	});

    $(".mobile-nav").click(function(){
        $(".mobile-options").slideToggle();   
    });

    $("#form").submit(function(e) {

        if (isSubmitting) return;

        isSubmitting = true;

        $(".page-pop-up").fadeIn();
        $.ajax({
            type: "POST",
            url: "/submit",
            data: $(this).serialize(),
            success: function(response){
                isSubmitting = false;
                $(".loading-icon").hide();
            },
            error: function(xhr) {
                isSubmitting = false;
                $(".loading-icon").hide();
            }
        })

    });

	$(".menu-item-click").click(function(){
		$(".page-pop-up").show();
	});
	
	$(".radio-buttons").click(function(){
		console.log($(this).val());
	});

    

	if ($(".survey-message").text().trim() != "") {
		$(".No-survey-message").css("display", "block");
	}

	if($("#sucess-message").text().trim() != ""){
		$(".server-feedback").fadeIn();
		$(".result-1").fadeIn();
	}

	if ($("#error-message").text().trim() != ""){
		$(".server-feedback").fadeIn();
		$(".result-2").fadeIn();
	}

	$(".logo-style").click(function(){
		 $(".server-feedback").fadeIn();
	});

	$(".server-feedback").click(function(){
		$(this).fadeOut();
	});

});