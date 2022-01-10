# main.py
# coding:utf-8
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL
app = Flask(__name__)

files = UploadSet('files', ALL)
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'

configure_uploads(app, files)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'media' in request.files:
        filename = files.save(request.files['media'])
        print('filename=',filename)
        url = files.url(filename)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5200,debug=True)
