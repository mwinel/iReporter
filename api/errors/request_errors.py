from flask import request, jsonify


class RequestError:
    """
    This class defines a way to handle request exceptions.

    ...

    Attributes
    ----------
    message
        the formatted error message

    Methods
    -------
    not_found
        returns a formatted 404 NOT FOUND message
    method_not_allowed
        returns a formatted 405 METHOD NOT ALLOWED message
    """

    message = {
        "error_message": "{0}, '{1}'"
    }

    def not_found(self):
        """
        returns a formatted 404 NOT FOUND message
        """
        return jsonify({
            "error": RequestError.message["error_message"].format(
                "404 Not Found: The requested URL was not found on the server",
                request.url
            )
        }), 404

    def method_not_allowed(self):
        """
        returns a formatted 405 METHOD NOT ALLOWED message
        """
        return jsonify({
            "error": RequestError.message["error_message"].format(
                "405 Method Not Allowed: The method is not allowed for the requested URL",
                request.url
            )
        }), 405
