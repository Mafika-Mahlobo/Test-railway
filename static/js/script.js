$(document).ready( function() {

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

	if ($(".survey-message").text().trim() != "") {
		$(".results-body-container").css("display", "none");
		$(".survey-message").css("display", "block");
	} 

	// $(this).delay(3000).fadeOut('slow');
});
	
