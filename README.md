jQuery/AJAX
=====================

In order to allow Ubermelon employees to interact with each other, we're
building a live message board application using Flask, HTML/CSS, and
Javascript.

Unfortunately, it's only half-completed. It's your job to read the code,
understand how it works, and complete it.

## Goal of the Application

The application is a "single-page application" (that is, there's only one web page
but it interacts with you using AJAX to update itself).

It has a textbox on the left where you can enter a message to send to the server
and an area on the right that lists all of the messages received.

## What Works Now

Right now, we have the basic Flask app written, along with the HTML and CSS.
We have some of the Javascript writen, but more work there needs to be done.

Currently, the application allows you to send a message using the left-hand
form. These messages are being sent to the server and stored in the session.

It does not currently read the messages the server has received, nor is there
code yet to update the messages-received list.

## Wall API

We have an API, working in our Flask app, for both getting the list of
messages and sending a new message.

### Getting Messages

The API for getting the messages is

```
http://localhost:5000/api/wall/get
```

This must be a GET request. It returns an array of message objects and an
"OK" result code:

```json
{
    "messages": [
      { "message": "I'm a message!" },
      { "message": "I'm another message." }
    ],
    "result": "OK"
}
```

### Sending a Message

The API for sending a message is

```
http://localhost:5000/api/wall/set
```

**You must also pass the POST parameter "m" and it must contain a valid
(non-blank message.**

You must make this as a POST request. It returns a JSON object
containing an array of message objects as well as a result message.
The array includes all of the messages, including the one you just sent.

For example:

```json
{
    "messages": [
      { "message": "I'm a message!" },
      { "message": "I'm the message you just sent." },
    ],
    "result": "Message received"
}
```

## Your Tasks

Get the server started by running the application from your command line
```
python js_webapp.py
```

### Get Initial Messages

Right now, we hardcode in some placeholder messages, but these should
really be requested from the server at the time the page is loaded.

Your task is to retrieve these messages using jQuery/AJAX and update the list
of messages. You should do this by manipulating the DOM to place these
message in the "message-container" list. You can see the HTML structure
required by looking at the placeholder messages in the HTML.

Once you've done this, **please request a code review.**

### Update the Messages

When a new message is posted, the message list should also be updated
to include new messages. You should update the "message-container"
to reflect the new list of messages.

Once you've done this, **please request a code review.**

### New Feature: Filtering Words

Once you've got your page sending and receiving messages and updating the
message wall, create a filter for your messages to take out naughty words
like "bad" and "ugly" and replace them with preferred words like
"good" and "awesome."

You could do this either on the client-side (in Javascript) or the
server-side (in Python). Which do you prefer? Why?

Once you've done this, **please request a code review.**

### New Feature: Prevent "Flooding"

We don't want to let users send dozens messages in a minute!

Add a time limit to how often you're allowed to set a new message.
Change the Javascript to require at least 10 seconds between sending
messages.

After you've done that, some things to think about: how secure is this?
Could a clever hacker get around this? What kinds of backup measures
could be taken to prevent someone from doing so?

Once you've done this, **please request a code review.**

### Escape or Remove HTML From Messages

We don't want to allow people to put HTML into the messages
themselves. That could open up a nasty security problem when these
messages show up on other people's browsers--especially if their
HTML included HTML script tags containing Javascript that was run!

- You might prefer to do this by removing HTML entirely, so a message
  like "I am a &lt;b&gt;hacker&lt;/b&gt;" becomes "I am a ".

- Or you could do it by "escaping" the HTML, where the HTML brackets
  are removed or changed into non-HTML-angle backets, so that message
  would become "I am a &amp;lt;b&amp;gt;hacker&amp;lt;/b&amp;gt;"
  (that would show them the brackets, but it wouldn't make the
  word hacker bold).

- Or you could remove the HTML tags but keep the text, so the message
  would become "I am a hacker".

Which of those do you prefer? Why?

You could do any of these in different ways. One way would be to use
the HTMLParser module in the Python standard library.

Once you've done this, **please request a code review.**

## Extra Credit/Advanced: Thinking Outside The Box

Currently, all stored messages are being sent from the server whether
or not you're setting of getting. Feel free to modify the server code
to possibly keep track of new messages by date and time, sequential order
or perhaps something entirely new. Once you've done that, is it really
necessary to send all the messages instead of just what the web page needs?
Think about how you can improve on the system.