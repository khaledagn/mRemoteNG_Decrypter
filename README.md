# mRemoteNG Decrypter

mRemoteNG Decrypter is a web application built with Flask that allows users to securely upload and decrypt XML or CSV files encrypted with mRemoteNG's password encryption feature. It provides a simple interface for uploading files, optionally specifying a password for decryption, and viewing the decrypted contents.

## Features

- Supports decryption of XML and CSV files encrypted with mRemoteNG.
- Securely handles file uploads and password input.
- Easy-to-use web interface.
- Provides feedback on successful decryption or errors encountered.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the web application in your browser at `http://localhost:5000`.
5. Upload an encrypted XML or CSV file.
6. Optionally, enter the password used for encryption.
7. Click on the "Upload" button.
8. View the decrypted contents on the result page.

## Requirements

- Python 3.x
- Flask
- Werkzeug
- Jinja2
- python-dotenv
- gunicorn
- pycryptodomex

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
