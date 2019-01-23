"""
incident validations class
"""


class IncidentValidations:
    """
    A class used to represent incident validations
    """

    def validate_incident_media(self, images, videos):
        """
        validates incident media inputs
        param: images, videos
        returns: error message
        """
        if not images or images.isspace():
            return "Image field cannot be left empty."
        if not images.endswith(('.jpeg', '.jpg', '.png')):
            return "Invalid image format."
        if not videos or videos.isspace():
            return "Video field cannot be left empty."
        if not videos.endswith(('.mp4', '.wmv', '.mkv', '.avi')):
            return "Invalid video format."


    def validate_incident_input(self, status, incident_type, location, comment):
        """
        validates incident input
        param: status, incident_type, location, comment
        returns: error message
        """
        if not status or status.isspace():
            return "Status field cannot be left empty."
        if not incident_type or incident_type.isspace():
            return "Incident Type field cannot be left empty."
        if not location or location.isspace():
            return "Location field cannot be left empty."
        if not comment or comment.isspace():
            return "Comment field cannot be left empty."
