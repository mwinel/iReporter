import datetime


class BaseRedFlag(object):
    """
    A class used to represent redflag base data.

    ...

    Attributes
    ----------
    status : str
        the status of the redflag e.g. draft
    image : str
        the image of the redflag
    video : str
        the video of the redflag
    comment : str
        the comment to the redflag
    created_on : str
        the date and time when the redflag is created
    created_by : str
        the username of the current_user

    Methods
    -------
    validate_base_redflag
        validates redflag input (status, image, video, comment,
        created_by, created_on)
    """

    def __init__(self, status, image, video, comment, created_by):
        """
        initialize redflag base attributes
        """
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
        self.created_on = datetime.datetime.now()
        self.created_by = created_by

    def validate_base_redflag(self):
        """
        validates redflag base inputs
        returns: error message
        """
        if not self.status or self.status.isspace():
            return "Status field cannot be left empty."
        if not self.image or self.image.isspace():
            return "Image field cannot be left empty."
        if not self.image.endswith(('.jpeg', '.jpg', '.png')):
            return "Invalid image format."
        if not self.video or self.video.isspace():
            return "Video field cannot be left empty."
        if not self.video.endswith(('.mp4', '.wmv', '.mkv', '.avi')):
            return "Invalid video format."
        if not self.comment or self.comment.isspace():
            return "Comment field cannot be left empty."


class RedFlag(object):
    """
    A class used to represent a RedFlag.

    ...

    Attributes
    ----------
    base : class
        inherits class BaseRedFlag attributes
    title : str
        the title of the redflag
    redflagType : str
        the type of the redflag
    location : str
        the location of the redflag
    id : int
        the redflag id

    Methods
    -------
    validate_redflag
        validates redflag input (title, redflagType, location)
    to_json
        returns redflag data in json serializable format
    """

    redflag_id = 1

    def __init__(self, base, title, redflag_type, location):
        """
        initialize redflag attributes
        """
        self.base = base
        self.title = title
        self.redflag_type = redflag_type
        self.location = location
        self.id = RedFlag.redflag_id
        RedFlag.redflag_id += 1

    def validate_redflag(self):
        """
        validates redflag input
        returns: error message
        """
        if not self.title or self.title.isspace():
            return "Title field cannot be left empty."
        if not self.redflag_type or self.redflag_type.isspace():
            return "Redflag Type field cannot be left empty."
        if not self.location or self.location.isspace():
            return "Location field cannot be left empty."

    @property
    def to_json(self):
        """
        returns redflag data in json serializable format
        """
        return {
            "id": self.id,
            "created_on": self.base.created_on,
            "created_by": self.base.created_by,
            "title": self.title,
            "type": self.redflag_type,
            "location": self.location,
            "status": self.base.status,
            "Images": self.base.image,
            "Videos": self.base.video,
            "comment": self.base.comment
        }
