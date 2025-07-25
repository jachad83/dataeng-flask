from flask import (
    Blueprint, request, make_response
)
from utils.pvdatacollect import PvGenerationData
from flaskr.db import get_db


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/pesregionlist', methods=['GET'])
def get_pes_region_list():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pesregion;')
    pes_regions = cur.fetchall()
    cur.close()
    conn.close()

    response_data = {}
    response_data['data'] = pes_regions

    response = make_response(response_data) # TODO: proper success and error handling
    response.status_code = 200
    response.mimetype = 'application/json'

    return response


@bp.route('/pvgen', methods=['GET'])
def set_pv_data():
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    conn = get_db()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM pv_{start_date}_{end_date};')
    gen_data = cur.fetchall()
    cur.close()
    conn.close()

    response_data = {}
    response_data['data'] = gen_data

    response = make_response(response_data) # TODO: proper success and error handling
    response.status_code = 200
    response.mimetype = 'application/json'

    return response

# TODO: post method to create new data
# @bp.route('/pvgen', methods=['POST'])
# def set_pv_data():
#     start_date = request.args.get('start')
#     end_date = request.args.get('end')
#     pv_gen_data = PvGenerationData(start_date.replace("_", "-"), end_date.replace("_", "-")) # TODO: standardise use of - and _ for date parsing

#     response = make_response('{"error": "Failed to save data to database"}')
#     response.status_code = 500
#     response.mimetype = 'application/json'

#     if pv_gen_data.pv_data_to_no_sql_db(): # TODO: proper success and error handling
#         if pv_gen_data.pv_no_sql_to_sql_db():
#             response = make_response('{"success": "Success saving data to database"}')
#             response.status_code = 201
#             response.mimetype = 'application/json'

#     return response