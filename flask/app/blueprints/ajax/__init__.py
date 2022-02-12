from flask import Blueprint
import json

bp_ajax = Blueprint('bp_ajax', __name__)

@bp_ajax.get('/helloworld')
def helloworld():
    result = { 'msg': 'hello world!' }
    return json.dumps(result)
