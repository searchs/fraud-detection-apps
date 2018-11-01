import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

__author__ = 'Ola Ajibode'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'tsv', 'sql'}

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, UPLOAD_FOLDER)
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for upp_file in request.files.getlist('file'):
        print(upp_file)
        filename = upp_file.filename
        destination = "/".join([target, filename])
        print(destination)
        upp_file.save(destination)

    return render_template('complete.html')


def clean_uploads():
    pass


def push_files_s3():
    pass


if __name__ == '__main__':
    # Remove files in upload dir
    app.run(host='127.0.0.1', port=8000, debug=True)
