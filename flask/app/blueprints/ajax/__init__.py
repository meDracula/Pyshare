from flask import Blueprint, request, session, abort
from flask_login import login_required, current_user
import json

bp_ajax = Blueprint('bp_ajax', __name__)

from app.controllers.post_controller import post_voting

@bp_ajax.post('/post_vote')
@login_required
def post_vote():
    result = request.get_json()
    vote = post_voting(result['title_hash'], result['vote'])
    return json.dumps({'rating': vote})

