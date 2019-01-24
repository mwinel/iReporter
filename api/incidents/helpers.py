"""
helper functions
"""
from db.database import DatabaseConnection

db = DatabaseConnection()


def get_by_redflag_type():
    """
    returns a list of redflags by redflag type
    """
    incident_type = 'red-flag'
    redflags = db.get_all_by_argument('incidents', 'incident_type', incident_type)
    return redflags
