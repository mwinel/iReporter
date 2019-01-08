import datetime

class BaseRedFlag:

    def __init__(self, status, image, video, comment):
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
        self.createdOn = datetime.datetime.now()


class RedFlag:

    redflag_id = 1

    def __init__(self, base, title, redflagType, location):
        self.base = base
        self.title = title
        self.redflagType = redflagType
        self.location = location
        self.id = RedFlag.redflag_id
        RedFlag.redflag_id += 1

    @property
    def to_json(self):
        return {
            "id": self.id,
            "createdOn": self.base.createdOn,
            "title": self.title,
            "type": self.redflagType,
            "location": self.location,
            "status": self.base.status,
            "Images": self.base.image,
            "Videos": self.base.video,
            "comment": self.base.comment
        }