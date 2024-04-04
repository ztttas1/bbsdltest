from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/files', methods=['GET'])
def list_files():
    files_directory = "bbs"
    files = os.listdir(files_directory)
    return jsonify(files)

@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory('bbs', filename)

if __name__ == '__main__':
    app.run(debug=True)
