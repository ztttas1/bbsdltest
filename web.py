from flask import Flask, render_template, send_from_directory, safe_join, abort
import os

app = Flask(__name__)

@app.route('/')
def list_files():
    directory = "bbs"
    files = os.listdir(directory)
    return render_template('list_files.html', files=files)

@app.route('/bbs/<filename>')
def file_content(filename):
    directory = safe_join(app.root_path, 'bbs')
    try:
        return send_from_directory(directory, filename)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
