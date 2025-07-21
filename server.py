from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/data')
def get_data():
    data = {"message": "Hello from the Python backend!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)