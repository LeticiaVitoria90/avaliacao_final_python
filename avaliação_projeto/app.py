from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

data = pd.read_csv('sales.superstore.csv')
data['Order_Date'] = pd.to_datetime(data['Order_Date'])
data['Ship_Date'] = pd.to_datetime(data['Ship_Date'])
data.fillna({'Postal_Code': 0}, inplace=True)

app = Flask(__name__)

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    try:
        stats = data.describe(include=[np.number]).to_dict()
        return jsonify({"statistics": stats}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    try:
        if record_id < 0 or record_id >= len(data):
            return jsonify({"error": "ID fora do intervalo válido."}), 404
        record = data.iloc[record_id].to_dict()
        return jsonify(record), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
