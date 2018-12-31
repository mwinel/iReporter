from flask import request, jsonify


class RequestError:
    """
    This class defines a way to handle request exceptions.
    """

    message = {
        "error_message": "{0}, '{1}'"
    }

    def not_found(self):
        return jsonify({
            "error": RequestError.message["error_message"].format(
                "404 Not Found: The requested URL was not found on the server",
                request.url
            )
        }), 404

    def method_not_allowed(self):
        return jsonify({
            "error": RequestError.message["error_message"].format(
                "405 Method Not Allowed: The method is not allowed for the requested URL", 
                request.url
            )
        }), 405