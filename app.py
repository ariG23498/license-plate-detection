# Dependencies
from flask import Flask, request, send_file
from PIL import Image

from TFOD_Flask import working

app = Flask(__name__)

@app.route('/')
def hello():
    return "TCS humAIn"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image 
    input_file = request.files.get('file')

    # Exception Handling
    if not input_file:
	    return "File is not present in the request"
    if input_file.filename == '':
	    return "Filename is not present in the request"
    if not input_file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
	    return "Invalid file type"
    
    else:
        im = working(input_file) #numpy array
        img = Image.fromarray(im)
        img.save("Flask.jpg")
        return send_file("Flask.jpg",mimetype = 'image/jpeg')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    app.run(port=port, debug=True)