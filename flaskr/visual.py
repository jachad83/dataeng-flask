from flask import (
    Blueprint, render_template
)

from flaskr.db import get_db


bp = Blueprint('visual', __name__, url_prefix='/visual')


@bp.route('/graph')
def graph():
    return render_template('visual/graph.html')