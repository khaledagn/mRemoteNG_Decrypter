from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import subprocess
import time

app = Flask(__name__)

# Set the upload folder and allowed file types
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xml'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file has the correct extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and decryption
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was submitted
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    # If no file is selected, return to the upload page
    if file.filename == '':
        return redirect(request.url)

    # If file has correct extension, save it and run decryption
    if file and allowed_file(file.filename):
        # Save the file with a timestamp
        filename = secure_filename(file.filename)
        filename_with_timestamp = f"{os.path.splitext(filename)[0]}_{int(time.time())}{os.path.splitext(filename)[1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_with_timestamp))

        # Get the password from the form
        password = request.form.get('password')

        # Construct the decryption command
        command = ['python3', 'decrypt_script.py']
        if password:
            command.extend(['-p', password])
        command.append(os.path.join(app.config['UPLOAD_FOLDER'], filename_with_timestamp))

        # Run the decryption script
        result = subprocess.run(command, capture_output=True, text=True)

        # Prepare decrypted data for template rendering
        if result.returncode == 0:
            decrypted_data = result.stdout.strip().split('\n')
            decrypted_data_with_index = [{'index': index + 1, 'line': line} for index, line in enumerate(decrypted_data)]
            return render_template('result.html', decrypted_data=decrypted_data_with_index)
        else:
            error_message = result.stderr.strip() if result.stderr else "An error occurred during decryption."
            return render_template('error.html', error_message=error_message)
    else:
        return render_template('error.html', error_message='Invalid file format')

if __name__ == '__main__':
    app.run(debug=True)
