"""
incident validations class
"""


class IncidentValidations:
    """
    A class used to represent incident validations
    """

    def validate_incident_input(self, status, incident_type, location, comment):
        """
        validates incident input
        param: status, incident_type, location, comment
        returns: error message
        """
        if not incident_type or incident_type.isspace():
            return "Incident Type field cannot be left empty."
        if not location or location.isspace():
            return "Location field cannot be left empty."
        if not comment or comment.isspace():
            return "Comment field cannot be left empty."
