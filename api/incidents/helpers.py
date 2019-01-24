"""
helper functions
"""
from db.database import DatabaseConnection

db = DatabaseConnection()


def get_redflags_by_redflag_type():
    """
    returns a list of incidents by redflag type
    """
    incident_type = 'red-flag'
    redflags = db.get_all_by_argument('incidents', 'incident_type', incident_type)
    return redflags


def get_interventions_by_intervention_type():
    """
    returns a list of incidents by interventions type
    """
    incident_type = 'intervention'
    interventions = db.get_all_by_argument('incidents', 'incident_type', incident_type)
    return interventions
