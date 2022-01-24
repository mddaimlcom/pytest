#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request, jsonify, abort
from common import DbHandler
from pathlib import Path


base_directory_path = Path(__file__).parent
app = Flask(__name__)
company_data_handler = DbHandler(str(base_directory_path / 'db.json'))


@app.errorhandler(400)
def handle_bad_request(e):
    print('Custom handler active')
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def handle_bad_request(e):
    print('Custom handler active')
    return jsonify(error=str(e)),  404


@app.route('/companies', methods=['GET'])
def get_company_records():
    company_id = request.args.get('id')
    data = company_data_handler.retrieve_data()
    if company_id is None:
        response = data
    else:
        response = [i for i in data if int(company_id) == i['id']]
        if len(response) == 0:
            abort(404, description="Resource not found. The company with id {} not found".format(company_id))
    return jsonify(response)


@app.route('/companies', methods=['POST'])
def create_company_records():
    payload = request.get_json(force=True)
    mandatory_keys = ('name', 'reg_num')
    payload_keys = payload.keys()
    filtered_keys = list(filter(lambda x: x in mandatory_keys, payload_keys))
    if len(filtered_keys) == 2:
        new_item_id = company_data_handler.send_data(payload)
        return jsonify(new_item_id)
    abort(400, description=f"Your request must have following keys {mandatory_keys}")


if __name__ == '__main__':
    import sys
    _port = sys.argv[1]  # get the port number to bind to passed from the cli arguments
    # start listening to the port for http requests in debug mode
    app.run(host='127.0.0.1', port=int(_port), debug=True)
    # app.run(host='127.0.0.1', port=_port)

