import os, shutil
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads, DOCUMENTS
from morse import Morse
# from process_img import ExtractColors
from threading import Thread
import subprocess
from weather import Weather
from text_to_speech import get_audio
from werkzeug.utils import secure_filename

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "123123123123dasdasd"
# app.config['UPLOADED_PHOTOS_DEST'] = "UPLOADS/photos"
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOADED_DOCUMENTS_DEST'] = 'UPLOADS/documents'
app.config['AUDIO_FOLDER'] = 'UPLOADS/audio'
# photos = UploadSet('photos', IMAGES)
documents = UploadSet('documents', DOCUMENTS)
# configure_uploads(app, photos)
configure_uploads(app, documents)
morse = Morse()
# extract_colors = ExtractColors()
weather_instance = Weather()


def empty(path):
    folder = f'UPLOADS/{path}'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


@app.route('/', methods=["POST", "GET"])
def homepage():
    return render_template("index.html")
    # return app.send_static_file("index.html")


@app.route('/morse', methods=["POST"])
def get_morse():
    if request.method == "POST":
        morse.reset()
        data = request.form.get("text")
        morse_output = morse.to_morse(data)
        return jsonify({"morse_output": morse_output})


# @app.route('/UPLOADS/photos/<filename>')
# def get_photo(filename):
#     return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route('/UPLOADS/documents/<filename>')
def get_pdf(filename):
    return send_from_directory(app.config['UPLOADED_DOCUMENTS_DEST'], filename)


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#

# @app.route('/upload', methods=['POST'])
# def upload():
#     if request.method == "POST":
#         empty("photos")
#         file = request.files['photo']
#         extract_colors.reset_extract_colors()
#         if file and allowed_file(file.filename):
#             filename = photos.save(file)
#             file_url = url_for("get_photo", filename=filename)
#             img_path = f"UPLOADS/photos/{filename}"
#             # dominant_colors, counts = extract_dominant_colors(img_path)
#             dominant_colors, counts = extract_colors.extract_dominant_colors(image_path=img_path)
#             dominant_colors = dominant_colors.tolist()
#             counts = counts.tolist()
#             return jsonify({"colors": dominant_colors, "counts": counts, "file_url": file_url})
#         else:
#             return jsonify({"error": "Invalid file type. Please choose a valid image file."})


@app.route('/open_tkinter_window', methods=['POST'])
def open_tkinter_window():
    thread = Thread(target=open_tkinter_app)
    thread.start()
    return jsonify({"message": "Tkinter window opened successfully"})


def open_tkinter_app():
    subprocess.run(['python', 'dangerousWriting.py'])


@app.route('/open_breakout_window', methods=['POST'])
def open_breakout_window():
    subprocess.Popen(['python', 'breakout/breakout.py'])
    return jsonify({"message": "Breakout window opened successfully"})


@app.route('/weather', methods=["POST"])
def weather():
    if request.method == "POST":
        temperature, condition, condition_icon, city, country = weather_instance.get_weather()
        response_data = {"temperature": temperature, "condition": condition, "icon": condition_icon, "city": city,
                         "country": country}
        return jsonify(response_data)


@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if request.method == "POST":
        empty("documents")
        empty("audio")
        file = request.files['pdf']
        secure_filename(file.filename)
        if file.content_type.startswith('application/pdf'):
            filename = documents.save(file)
            # file_url = url_for("get_pdf", filename=filename)
            pdf_path = f"UPLOADS/documents/{filename}"
            audio_url = get_audio(pdf=pdf_path)
            return jsonify({"audio_url": audio_url})
        else:
            return jsonify({"Error": "Please Upload Pdf"})


@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)


if __name__ == "__main__":
    app.run()

# host="0.0.0.0",port=5000
