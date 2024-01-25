# Install required packages:
# pip install Flask Pillow

from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        # Get the uploaded image file
        image = request.files['image']

        # Check if the file is an image
        if image and image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Convert image to PDF
            pdf_path = convert_to_pdf(image)

            # Send the PDF file for download
            return send_file(pdf_path, as_attachment=True)

    except Exception as e:
        return str(e)

def convert_to_pdf(image):
    # Open the image using Pillow
    img = Image.open(image)

    # Convert image to PDF
    pdf_path = 'converted_file.pdf'
    img.save(pdf_path, 'PDF', resolution=100.0, save_all=True)

    return pdf_path

if __name__ == '__main__':
    app.run(debug=True)

