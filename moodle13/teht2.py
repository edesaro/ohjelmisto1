from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_info(icao_code):
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, municipality FROM airports WHERE ident=?", (icao_code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"ICAO": icao_code, "Name": row[0], "Municipality": row[1]}
    else:
        return None

@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def airport_info(icao_code):
    info = get_airport_info(icao_code)
    if info:
        return jsonify(info)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)