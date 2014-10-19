"""API for JS Webapp Wall application.

In real life, for us to share messages between different users of this
application, we'd want to store the messages in a server-side persistent
store (like a relational database). However, since we're demonstrating how
to use client-side session systems, this stores things there.
"""


from flask import session

# So that you can play with the `get` API, we return a single
# test message as the default.
DEFAULT_MESSAGES = [
    {'message': 'First message.'},
]


class Api(object):
    """API for messages application."""

    def error(self, error):
        """Handle API errors.

            error: (string) error message

            returns: dictionary error object.
        """

        return  {
            "result": error,
        }

    def get(self):
        """Get messages.

            returns: dictionary with messages list + result code.
        """

        return {
            "result": "OK",
            "messages": session.get('wall', DEFAULT_MESSAGES),
        }

    def set(self, msg):
        """Set a new message.

            msg: (string) message

            returns: dictionary with messages list + result code.
        """

        wall_dict = {
            "message": msg,
        }

        session.setdefault('wall', []).append(wall_dict)

        result = self.get()
        result["result"] = "Message Received"

        return result
