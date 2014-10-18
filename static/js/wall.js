$(document).ready(function () {
    // Normally, JavaScript runs code at the time that the <script>
    // tags loads the JS. By putting this inside a jQuery $(document).ready()
    // function, this code only gets run when the document finishing loading.
	initWallApplication();
});

/**
 * The init function is run once the document is
 * completely loaded (and drunk).
 */
function initWallApplication() {
	$("#message-form").submit(function (e) {
		e.preventDefault();
		
		console.log("Submitting new message.");
		var url = "/api/wall/set";
    	sendMessageDataToServer(this, url);

		// Reset the message container to be empty
		$("#message").val("");
	});
}

/*
 * This function makes the AJAX call to the server
 * and passes the message to it.
 */
function sendMessageDataToServer(formObj, url) {
	// Send the message data to the server to be stored
	$.ajax({
		dataType: "json",
		url: url,
		type: 'POST',
		data: $(formObj).serialize(),
		success: function (data) {
			console.log("sendMessageDataToServer: ", data);
			showTempResultMessage(data.result);
		}
	});
}

/*
 * This is a helper function that does nothing but show a section of the
 * site (the message result) and then hide it a moment later.
 */
function showTempResultMessage(resultMsg) {
    var notificationArea = $("#sent-result");
    notificationArea.text(resultMsg);
    notificationArea.slideDown(function () {
        // In JavaScript, "this" is a keyword that means "the object this
        // method or function is called on"; it is analogous to Python's
        // "self". In our case, "this" is the #sent-results element, which
        // is what slideDown was called on.
        //
        // However, when setTimeout is called, it won't be called on that
        // same #sent-results element--"this", for it, wouldn't be that
        // element. We could put inside of our setTimeout call the code
        // to re-find the #sent-results element, but that would be a bit
        // inelegant. Instead, we'll use a common JS idiom, to set a variable
        // to the *current* definition of self, here in this outer function,
        // so that the inner function can find it and where it will have the
        // same value. When stashing "this" into a new variable like that,
        // many JS programmers use the name "self"; some others use "that".
		var self = this;

		setTimeout(function () {
			$(self).slideUp();
		}, 2000);
	});
}