import io,base64
import pprint

from flask import (
    Blueprint, request, render_template
)

from flaskr.db import get_db
from matplotlib.figure import Figure


bp = Blueprint('visual', __name__, url_prefix='/visual')


@bp.route('/graph')
def graph():
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    conn = get_db()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM pv_{start_date}_{end_date};')
    gen_data = cur.fetchall()
    cur.close()
    conn.close()

    parsed_data_10 = [x[0] for x in gen_data]
    parsed_data_11 = [x[1] for x in gen_data]
    parsed_data_12 = [x[2] for x in gen_data]
    parsed_data_13 = [x[3] for x in gen_data]
    parsed_data_14 = [x[4] for x in gen_data]

    fig = Figure()
    ax = fig.subplots()
    ax.plot(parsed_data_10)
    ax.plot(parsed_data_11)
    ax.plot(parsed_data_12)
    ax.plot(parsed_data_13)
    ax.plot(parsed_data_14)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"