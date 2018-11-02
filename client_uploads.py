import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

__author__ = 'Ola Ajibode'

UPLOAD_FOLDER = 'uploads'
global upload_queue
upload_queue = []
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT, UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'csv', 'tsv', 'sql'}

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(os.listdir(target))
    clean_uploads(target)

    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # target = os.path.join(APP_ROOT, UPLOAD_FOLDER)
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    clean_uploads(target)

    for upp_file in request.files.getlist('file'):
        print(upp_file)
        filename = upp_file.filename
        destination = "/".join([target, filename])
        print(destination)
        upp_file.save(destination)

    upqueue = os.listdir(target)
    print(upqueue)

    return render_template('complete.html')


def clean_uploads(target):
    upload_queue = os.listdir(target)
    print(upload_queue)
    if len(upload_queue) > 0:
        for f in upload_queue:
            os.remove(os.path.join(target,f))
    upload_queue = os.listdir(target)
    print(upload_queue)




def push_files_s3():
    pass


if __name__ == '__main__':
    # Remove files in upload dir
    app.run(host='127.0.0.1', port=8000, debug=True)
