from flask import render_template, current_app, send_from_directory, send_file
from app.main import bp
import qrcode
import os

@bp.route('/')
def index():
    result = ['Sergio', 'Rodrigo', 'Cardenas', 'Rivera']
    return render_template('index.html', data=result)

@bp.route('/qrgenerator')
def qr_generator()->None:
    text_for_qr = "this is a text for qr code"
    img = qrcode.make(text_for_qr)
    img.save("app/qr_generated/qrcode1.png")
    return '<h1>qr generated</h1>'

@bp.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    folder='static'
    uploads = os.path.join(
        current_app.root_path,
        folder,
        'qr_generated'
        # app.config['UPLOAD_FOLDER']
    )
    # print(uploads)
    # filename_to_download = filename[0:filename.find(' '):]
    # print(filename_to_download)
    # Returning file from appended path
    # return send_from_directory(directory=uploads,path=filename)
    return send_file(download_name=filename, path_or_file=uploads+'/'+filename, as_attachment=True)
    # return render_template('index.html')