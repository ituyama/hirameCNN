import numpy as np

from PIL import Image
import os
import tensorflow as tf
new_model = tf.keras.models.load_model('my_model')
new_model.summary()
filepath='nkns.jpg'
image = np.array(Image.open(filepath).convert('RGB').resize((100, 100)))
print(filepath)
index=np.argmax(new_model.predict(np.array([image / 255.])))

# result = model.predict_classes(np.array([image / 255.]))
label_name=['ヒラメ','カレイ']
print('result:', label_name[index])
