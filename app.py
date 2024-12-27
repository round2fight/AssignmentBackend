import json
from flask_cors import CORS
from flask import Flask, jsonify,request

app = Flask(__name__)
CORS(app)

with open('files/device.json') as f:
    devices = json.load(f)

with open('files/fault.json') as f:
    faults = json.load(f)

@app.route('/api/home', methods=['GET'])
def home():
    return jsonify(message="Hello World")

@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify(devices)

@app.route('/api/faults', methods=['GET'])
def get_faults():
    return jsonify(faults)
    # windfarm = request.args.get('windfarm')
    # device_id = request.args.get('device_id')
    # fault_type = request.args.get('fault_type')

    # filtered_faults = faults

    # if windfarm:
    #     filtered_faults = [
    #         f for f in filtered_faults
    #         if any(d['asset'] == windfarm and d['id'] == f['device_id'] for d in devices)
    #     ]
    # if device_id:
    #     filtered_faults = [f for f in filtered_faults if str(f['device_id']) == device_id]
    # if fault_type:
    #     filtered_faults = [f for f in filtered_faults if f['fault_type'] == fault_type]

    # return jsonify(filtered_faults)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Ensure it listens on all interfaces