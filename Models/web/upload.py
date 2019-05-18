import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the read that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)
# This is the path to the upload directory
app.config[ 'UPLOAD_FOLDER' ] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config[ 'ALLOWED_EXTENSIONS' ] = set(['jpg', 'jpeg' ])


# For a given read, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[ 1 ] in app.config[ 'ALLOWED_EXTENSIONS' ]


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the read upload
@app.route('/upload', methods=[ 'POST' ])
def upload():
    # Get the name of the uploaded files
    num_1=request.form.get("Fuzzy")
    num_2=request.form.get("Accurate")
    # uploaded_files = request.files.getlist("read[]")
    filenames = [ ]
    if num_1:

        return render_template('upload.html', filenames=filenames)
    if num_2:

        return render_template('upload.html', filenames=filenames)

    #
    # for read in uploaded_files:
    #     # Check if the read is one of the allowed types/extensions
    #     if read and allowed_file(read.filename):
    #         # Make the filename safe, remove unsupported chars
    #         filename = secure_filename(read.filename)
    #         # Move the read form the temporal folder to the upload
    #         # folder we setup
    #         read.save(os.path.join(app.config[ 'UPLOAD_FOLDER' ], filename))
    #         # Save the filename into a list, we'll use it later
    #         filenames.append(filename)
    #         # Redirect the user to the uploaded_file route, which
    #         # will basicaly show on the browser the uploaded read
    # # Load an html page with a link to each uploaded read
    # return render_template('upload.html', filenames=filenames)


# This route is expecting a parameter containing the name
# of a read. Then it will locate that read on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config[ 'UPLOAD_FOLDER' ],
                               filename)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port="8080",
        debug=True)