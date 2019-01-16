import datetime

class BaseRedFlag:

    def __init__(self, status, image, video, comment, created_by):
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
        self.created_on = datetime.datetime.now()
        self.created_by = created_by
   
    def validate_base_redflag(self):
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


class RedFlag:

    redflag_id = 1

    def __init__(self, base, title, redflagType, location):
        self.base = base
        self.title = title
        self.redflagType = redflagType
        self.location = location
        self.id = RedFlag.redflag_id
        RedFlag.redflag_id += 1

    def validate_redflag(self):
        if not self.title or self.title.isspace():
            return "Title field cannot be left empty."
        if not self.redflagType or self.redflagType.isspace():
            return "Redflag Type field cannot be left empty."
        if not self.location or self.location.isspace():
            return "Location field cannot be left empty."

    @property
    def to_json(self):
        return {
            "id": self.id,
            "created_on": self.base.created_on,
            "created_by": self.base.created_by,
            "title": self.title,
            "type": self.redflagType,
            "location": self.location,
            "status": self.base.status,
            "Images": self.base.image,
            "Videos": self.base.video,
            "comment": self.base.comment
        }