import os

from flask import Flask, render_template, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename
from flask_s3 import FlaskS3

__author__ = 'Ola Ajibode'

ALLOWED_EXTENSIONS = {'csv', 'tsv', 'sql'}
UPLOAD_FOLDER = 'uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, UPLOAD_FOLDER)

upload_queue = os.listdir(target)

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'reports-adhoc-raw'
s3 = FlaskS3(app)


@app.route('/')
@app.route('/index')
def index():
    print(dir(s3.init_app))
    if len(upload_queue) > 0:
        clean_uploads(target)
    return render_template('index.html', title='Ingest File Upload')


@app.route('/upload', methods=['POST'])
def upload():
    if not os.path.isdir(target):
        os.mkdir(target)

    if len(request.files.getlist('file')) == 0:
        # TODO: Remove print, move to logger
        print("No file selected for upload.  Reloading page.....")
        return render_template('index.html', title='No File Selected')

    for upp_file in request.files.getlist('file'):
        filename = upp_file.filename
        destination = "/".join([target, filename])
        # Remove print, move to logger
        print(destination)
        upp_file.save(destination)

    upqueue = os.listdir(target)
    return render_template('complete.html', upload_list=upqueue, title='Upload Status')


def clean_uploads(target):
    upload_queue = os.listdir(target)
    # Remove print, move to logger
    if len(upload_queue) > 0:
        for f in upload_queue:
            os.remove(os.path.join(target, f))
    upload_queue = os.listdir(target)

    if len(upload_queue) > 0:
        print("Remove file failed. Upload dir still contains files.")


def push_files_s3():
    pass


if __name__ == '__main__':
    # Remove files in upload dir
    app.run(host='127.0.0.1', port=8000, debug=True)
