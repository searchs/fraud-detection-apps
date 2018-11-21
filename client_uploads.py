from __future__ import print_function
import os


from flask import render_template, request, flash
from programmatic_self_uploader import app

ALLOWED_EXTENSIONS = {'csv', 'tsv'}
UPLOAD_FOLDER = 'uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(APP_ROOT, UPLOAD_FOLDER)

if not os.path.isdir(TARGET):
    os.mkdir(TARGET)

UPLOAD_QUEUE = os.listdir(TARGET)
RAW_BUCKET = 'adhoc-raw'
S3_BUCKET = "lytics-programmatic-automation-report"


@app.route("/", methods=["GET"])
def index():
    if UPLOAD_QUEUE:
        clean_uploads()
    return render_template('index.html',
                           env=app.config['ohprice_environment'],
                           title='Raw File Upload')


@app.route('/upload', methods=['POST'])
def upload():
    if not os.path.isdir(TARGET):
        os.mkdir(TARGET)

    try:
        clean_uploads()
    except OSError:
        flash('File not found in directory or no directory: {}'.format(TARGET))

    target_date = request.form['report-date']
    report_type = request.form['selectProcess']

    if report_type == 'Rerun A Report':
        flash("No new data hence no upload necessary")
        upload_details, message = rerun_report()
    elif report_type == 'Run New Report':
        upload_details, message = run_new_report()

    flash(upload_details)

    if not any(upload_details):
        flash("Empty params!")
        message = "No file uploaded or no date supplied.  Try again."
        return render_template('index.html',
                               env=app.config['ohprice_environment'],
                               message=message)

    return render_template('complete.html',
                           env=app.config['ohprice_environment'],
                           title='Upload Status',
                           target_date=target_date,
                           upload_details=upload_details,
                           message=message)


def run_new_report():
    upload_details = dict()
    try:
        for upp_file in request.files.getlist('file'):
            filename = upp_file.filename
            destination = "/".join([TARGET, filename])
            upp_file.save(destination)
            details = dict()
            details['filesize'] = round(float(os.stat(destination).st_size / 1024 / 1024), 2)
            details['target_date'] = request.form['report-date']
            details['lookback'] = request.form['lookback']
            upload_details[filename] = details
            print(upload_details)

        if upload_details:
            message = "Upload Successful! "
        else:
            message = "No file selected.  Try again please."

    except OSError:
        message = "No file selected. No file uploaded."
        print("File does not exists in uploads directory!")
    return upload_details, message


def rerun_report():
    report_details = {}
    details = dict()
    details['target_date'] = request.form['report-date']
    details['lookback'] = request.form['lookback']
    report_details['rerun'] = details
    print(report_details)
    message = "Report Rerun is now in progress..."

    return report_details, message


@app.route('/check', methods=['GET'])
def check():
    return render_template('check.html',
                           title='App Status',
                           env=app.config['ohprice_environment'])


@app.errorhandler(404)
def page_not_found(error):
    # note that we set the 404 status explicitly
    return render_template('404.html',
                           message=error,
                           env=app.config['ohprice_environment']), 404


def clean_uploads():
    upload_queue = os.listdir(TARGET)
    if upload_queue:
        for item in upload_queue:
            os.remove(os.path.join(TARGET, item))
        upload_queue = os.listdir(TARGET)

    if upload_queue:
        print("Remove file failed. Upload dir still contains files.")
