from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/gas-stations')
def get_gas_stations():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    
    url = "http://www.opinet.co.kr/api/aroundAll.do"
    params = {
        'code': 'F241106421',
        'x': lng,
        'y': lat,
        'radius': 3000,
        'sort': 1,
        'prodcd': 'D047',
        'out': 'json'
    }
    
    try:
        response = requests.get(url, params=params)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)