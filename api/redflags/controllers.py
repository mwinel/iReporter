"""
Redflag controller
"""

from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from api.redflags.models import RedFlag, BaseRedFlag
from db.database import RedflagsDb

redflags = RedflagsDb()


class RedFlagsController:
    """
    A class used to represent the redflags controller

    ...

    Methods
    ----------
    create_redflag
        creates a redflag
    fetch_all_redflags
        returns a list of all redflags
    update_redflag(redflag_id)
        updates a redflag given its id
    fetch_redflag(redflag_id)
        returns a single redflag given its id
    delete_redflag(redflag_id)
        deletes a redflag from the redflags_list
    """

    def create_redflag(self):
        """
        creates a redflag
        """
        current_user = get_jwt_identity()
        data = request.get_json()
        title = data.get('title')
        redflag_type = data.get('redflag_type')
        location = data.get('location')
        status = data.get('status')
        image = data.get('image')
        video = data.get('video')
        comment = data.get('comment')
        created_by = current_user

        redflag = RedFlag(BaseRedFlag(status, image, video, comment, created_by),
                          title, redflag_type, location)

        validate_base = redflag.base.validate_base_redflag()
        validate_redflag = redflag.validate_redflag()
        if validate_base:
            return jsonify({
                "status": 400,
                "error": validate_base
            }), 400

        if validate_redflag:
            return jsonify({
                "status": 400,
                "error": validate_redflag
            }), 400

        redflags.add_redflag(redflag)
        return jsonify({
            "status": 201,
            "message": "Redflag successfully created.",
            "data": redflag.to_json
        }), 201

    def fetch_all_redflags(self):
        """
        returns a list with all redflags
        """
        all_redflags = [i.to_json for i in redflags.get_all_redflags()]
        return jsonify({
            "status": 200,
            "message": "success",
            "data": all_redflags
        }), 200

    def update_redflag(self, redflag_id):
        """
        updates a redflag given its id
        """
        redflag = [i.to_json for i in redflags.get_all_redflags() if i.id == redflag_id]
        if redflag:
            data = request.get_json()
            redflag[0]['title'] = data.get('title', redflag[0]['title'])
            redflag[0]['type'] = data.get('redflag_type', redflag[0]['type'])
            redflag[0]['location'] = data.get('location', redflag[0]['location'])
            redflag[0]['status'] = data.get('status', redflag[0]['status'])
            redflag[0]['Images'] = data.get('image', redflag[0]['Images'])
            redflag[0]['Videos'] = data.get('video', redflag[0]['Videos'])
            redflag[0]['comment'] = data.get('comment', redflag[0]['comment'])

            redflags.add_redflag(redflag)
            return jsonify({
                "status": 200,
                "message": "Redflag successfully updated.",
                "data": redflag
            }), 200

        return jsonify({
            "status": 200,
            "message": "Redflag was not found."
        }), 200

    def fetch_redflag(self, redflag_id):
        """
        returns a single redflag given its id
        """
        redflag = [i.to_json for i in redflags.get_all_redflags() if i.id == redflag_id]
        if redflag:
            return jsonify({
                "status": 200,
                "message": "success",
                "data": redflag
            }), 200
        return jsonify({
            "status": 200,
            "message": "Sorry! Redflag was not found."
        }), 200

    def delete_a_redflag(self, redflag_id):
        """
        deletes a redflag from a redflags_list
        """
        for redflag in redflags.get_all_redflags():
            if redflag.id == redflag_id:
                redflags.redflags_list.remove(redflag)
                return jsonify({
                    "status": 200,
                    "message": "Redflag successfully deleted."
                }), 200
        return jsonify({
            "status": 200,
            "message": "Redflag was not found."
        }), 200
