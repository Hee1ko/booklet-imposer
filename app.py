#!/usr/bin/env python3
from flask import Flask, request, send_file, render_template, Response
from werkzeug.utils import secure_filename
import os
import tempfile
from booklet_imposer import create_booklet

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'pdf' not in request.files:
        return {'error': 'No file uploaded'}, 400
    
    file = request.files['pdf']
    if file.filename == '':
        return {'error': 'No file selected'}, 400
    
    if not file.filename.lower().endswith('.pdf'):
        return {'error': 'File must be a PDF'}, 400
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = os.path.join(tmpdir, secure_filename(file.filename))
            output_path = os.path.join(tmpdir, 'booklet_' + secure_filename(file.filename))
            
            file.save(input_path)
            create_booklet(input_path, output_path)
            
            with open(output_path, 'rb') as f:
                pdf_data = f.read()
            
            return Response(
                pdf_data,
                mimetype='application/pdf',
                headers={'Content-Disposition': f'attachment; filename=booklet_{secure_filename(file.filename)}'}
            )
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
