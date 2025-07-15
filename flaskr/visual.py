import io,base64

from flask import (
    Blueprint, render_template
)

from flaskr.db import get_db
from matplotlib.figure import Figure


bp = Blueprint('visual', __name__, url_prefix='/visual')


# @bp.route('/graph')
# def graph():
#     return render_template('visual/graph.html')


@bp.route('/graph')
def graph():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"