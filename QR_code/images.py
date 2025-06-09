from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Path to the folder where images are stored
IMAGE_FOLDER = os.path.join('static', 'images')

# Route to serve the HTML page
@app.route('/')
def index():
    # List of images in the folder (you can add more images here)
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    return render_template('index.html', images=images)

# Route to serve static images from the folder
@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)