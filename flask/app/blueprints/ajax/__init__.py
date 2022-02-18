from flask import Blueprint, request, session, abort
from flask_login import login_required, current_user
from app.controllers.post_controller import post_voting
import json

bp_ajax = Blueprint('bp_ajax', __name__)


@bp_ajax.post('/post_vote')
@login_required
def post_vote():
    result = request.get_json()
    vote = post_voting(result['title_hash'], result['vote'])
    return json.dumps({'rating': vote})
