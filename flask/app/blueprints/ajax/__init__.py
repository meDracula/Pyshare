from flask import Blueprint, request, session, abort
from flask_login import login_required, current_user
import json

bp_ajax = Blueprint('bp_ajax', __name__)

from app.controllers.post_controller import post_voting

@bp_ajax.post('/post_vote')
@login_required
def post_vote():
    result = request.get_json()
    result = post_voting(result['title_hash'], result['vote'])
    if not result:
        return json.dumps({}), 406
    return json.dumps({'acknowledged': result}), 200

