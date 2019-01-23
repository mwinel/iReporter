"""
incident models
"""
class BaseIncident:
    """
    A class used to represent incident base data.

    ...

    Attributes
    ----------
    status : str
        the status of the incident e.g. draft
    image : str
        the image of the incident
    video : str
        the video of the incident
    comment : str
        the comment to the incident
    created_on : str
        the date and time when the incident is created
    created_by : str
        the username of the current_user

    """

    def __init__(self, status, image, video, comment):
        """
        initialize incident base attributes
        """
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment


class Incident:
    """
    A class used to represent a incident.

    ...

    Attributes
    ----------
    base : class
        inherits class BaseIncident attributes
    title : str
        the title of the incident
    incidentType : str
        the type of the incident
    location : str
        the location of the incident
    id : int
        the incident id
    """

    def __init__(self, base, incident_type, location):
        """
        initialize incindent attributes
        """
        self.base = base
        self.incident_type = incident_type
        self.location = location
