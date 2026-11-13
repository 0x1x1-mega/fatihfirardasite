import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

# Dosyaların saklandığı klasörün yolu
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/indir')
def download_page():
    return render_template('download.html')

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        # send_from_directory dosyayı güvenli bir şekilde gönderir
        # as_attachment=True parametresi dosyanın tarayıcıda açılmasını değil, doğrudan indirilmesini sağlar
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, description="Dosya bulunamadı.")

@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")

@app.route("/owners")
def owners():
    return render_template("creds.html")

@app.route("/game")
def web_game():
    return render_template("game.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)