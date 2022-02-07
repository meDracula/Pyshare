from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
bp_admin = Blueprint('bp_admin', __name__)

@bp_admin.get('/admin')
@login_required
def admin_page():
    return render_template('admin.html')

