from flask import session


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
            "messages": session.get('wall'),
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
