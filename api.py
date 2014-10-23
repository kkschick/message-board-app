"""API for JS Webapp Wall application.

In real life, for us to share messages between different users of this
application, we'd want to store the messages in a server-side persistent
store (like a relational database). However, since we're demonstrating how
to use client-side session systems, this stores things there.
"""
from flask import session
from HTMLParser import HTMLParser

# So that you can play with the `get` API, we return a single
# test message as the default.

DEFAULT_MESSAGES = [
    {'message': 'Welcome! (this is the built-in first message)'},
]


def wall_error(error):
    """Handle API errors.

        error: (string) error message

        returns: dictionary error object.
    """

    return {
        "result": error,
    }


def wall_list():
    """Get messages.

        returns: dictionary with messages list + result code.
    """

    return {
        "result": "OK",
        "messages": session.setdefault('wall', DEFAULT_MESSAGES),
    }

def wall_last():
    """ Return a dictionary with the result code and the last message submitted."""

    return session["wall"][-1]["message"]


def wall_add(msg):
    """Set a new message.

        msg: (string) message

        returns: dictionary with messages list + result code.
    """

    parser = RemoveHTML()
    parser.feed(msg)
    msg = parser.out

    wall_dict = {
        "message": msg,
    }

    session.setdefault('wall', []).append(wall_dict)

    result = wall_list()
    result["result"] = "Message Received"

    return result

def wall_clear():
    session["wall"] = DEFAULT_MESSAGES

    result = wall_list()
    result["result"] = "Wall Cleared"

    return result

class RemoveHTML(HTMLParser):
    out = ""
    def handle_data(self,data):
        self.out = self.out + data
