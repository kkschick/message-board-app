$(document).ready(function()
{
	init();
});

/**
 * The init function is run once the document is
 * completely loaded (and drunk).
 */
function init()
{
	$("#message-form").submit(function(e)
	{
		e.preventDefault();
		
		console.log("Submitting new message.");

		var self = this;

		sendMessageDataToServer(self);

		// Reset the message container to be empty
		$("#message").val("");
	});
}

/*
 * This function makes the AJAX call to the server
 * and passes the message to it.
 */
function sendMessageDataToServer(formObj)
{
	var url = "/api/wall/set";
	// Send the message data to the server to be stored
	$.ajax({
		dataType: "json",
		url: url,
		type: 'POST',
		data: $(formObj).serialize(),
		success: function(data)
		{
			console.log(data);
			$("#sent-result").text(data.result);

			showTempResultMessage();
		}
	});
}

/*
 * This is a helper function that does nothing but
 * show a section of the site (the message result)
 * and then hide it a moment later.
 */
function showTempResultMessage()
{
	$("#sent-result").slideDown(function()
	{
		var self = this;
		setTimeout(function()
		{
			$(self).slideUp();
		}, 2000);
	});
}