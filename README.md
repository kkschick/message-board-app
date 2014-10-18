jQuery/AJAX
=====================

Here we have a half built app and it's your task to complete it.

## What Works Now

Currently, the app allows you to send messages to the server and they are stored in the session.

#### Set Messages

An API is available
```
http://localhost:5000/api/wall/set
```
**You must also pass the POST parameter, "m", and it must contain a valid message.**

When you call this API, a JSON object containing an array of message objects as well as a result message is returned.

Example JSON result
```json
{
    "messages": [{
        "message": "I'm a message!"
    }, {
		"message": "I'm the message you just sent."
    }],
    "result": "Message received"
}
```

## Your Tasks

Get the server started by running the app from your command line
```
python js_webapp.py
```

### Get Messages

An API is available
```
http://localhost:5000/api/wall/get
```
**No other parameters are required to get this API call to return.**

When you call this API, a JSON object containing an array of message objects as well as a result message is returned.

Example JSON result
```json
{
    "messages": [{
        "message": "I'm a message!"
    }, {
		"message": "I'm another message!"
    }],
    "result": "OK"
}
```

Your task is to retrieve these messages using jQuery and AJAX and while manipulating the DOM, place them onto the page in the "message-container".

This should be done when the page is loaded.

### Update the Messages

Once you've started retrieving messages from the server (after you've made some new ones) you need to update the "message-container" with new messages being made.

The result of the API when sending messages is the entire list of messages being stored. It is up to you to update the "message-container" with these messages.

### Adding Features

Below are some features you should add to your Message Wall app.

#### Filtering Blacklisted Words

Once you've got your page sending and receiving messages and updating the message wall, create a filter for your messages to take out naughty words like "bad" and "ugly" and replace them with whitelisted words like "good" and "awesome."

#### Prevent Flooding

Add a time limit to how often you're allowed to set a new message. Since you know Python so well, make sure to implement the timer in JavaScript. Sure, you would be able to get around this measure but it'll be a good first line of defense against the flood of messages.

#### Add An Escape Mechanism

Prevent people who send messages from posting malicious code like JavaScript and HTML. A way to get rid of HTML would be to use the HTMLParser module in Python. Think of other methods you could use to prevent invalid messages from being sent and stored.

## Thinking Outside The Box

Currently, all stored messages are being sent from the server whether or not you're setting of getting. Feel free to modify the server code to possibly keep track of new messages by date and time, seuential order or perhaps something entirely new. Also, is it really nessisary to send all the messages instead of just what the web page needs? Think about how you can improve on the system.