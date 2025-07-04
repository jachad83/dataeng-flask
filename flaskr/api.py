import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from utils.pvdatacollect import PvGenerationData
from flaskr.db import get_db


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/pesregionlist')
def get_pes_region_list():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pesregion;')
    pes_regions = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(pes_regions)


@bp.route('/pvgen/<start_date>/<end_date>')
def set_pv_data(start_date, end_date):
    pv_gen_data = PvGenerationData(start_date, end_date)
    pv_gen_data.pv_data_to_no_sql_db()
    pv_gen_data.pv_no_sql_to_sql_db()
    return jsonify({
        'message': 'PV generation data for ${start_date} to ${end_date} extracted.'
    })