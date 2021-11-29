from flask import Flask,render_template,request,redirect,url_for,flash 
import numpy as np

from PIL import Image
import os
import tensorflow as tf
from flask import send_from_directory

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(__name__)
def tensols(url):
    
    new_model = tf.keras.models.load_model('my_model')
    new_model.summary()
    filepath=url
    image = np.array(Image.open(filepath).convert('RGB').resize((100, 100)))
    print(filepath)
    index=np.argmax(new_model.predict(np.array([image / 255.])))

    # result = model.predict_classes(np.array([image / 255.]))
    label_name=['ヒラメ','カレイ']
    return label_name[index]


@app.route('/', methods=['GET', 'POST'])
def hello():
    name = "Hello World"
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def good():
    fs = request.files['file']

    
    filename = fs.filename

    img_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    fs.save(img_url)
    name = "Good"
    rabel=tensols(img_url)
    return render_template("result.html",url=img_url,rabel=rabel)
    
@app.route('/uploads/<filename>')
# ファイルを表示する
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
## おまじない
if __name__ == "__main__":
    app.run()