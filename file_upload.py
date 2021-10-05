from werkzeug.utils import secure_filename
from flask import request, Flask

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.file['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f'/var/www.uploads/{secure_filename(file.filename)}')
